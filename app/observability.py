"""
OpenTelemetry and logging configuration for ELK stack integration.
"""
import logging
import sys
from typing import Optional
import uuid
from contextvars import ContextVar

import structlog
from opentelemetry import trace, metrics
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.sdk.metrics import MeterProvider
from opentelemetry.sdk.metrics.export import PeriodicExportingMetricReader
from opentelemetry.sdk.resources import Resource
from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.instrumentation.httpx import HTTPXClientInstrumentor
from opentelemetry.instrumentation.requests import RequestsInstrumentor
from opentelemetry.instrumentation.logging import LoggingInstrumentor
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError as ESConnectionError

from app.config import settings

# Context variables for request tracing
request_id_var: ContextVar[Optional[str]] = ContextVar("request_id", default=None)
trace_id_var: ContextVar[Optional[str]] = ContextVar("trace_id", default=None)
span_id_var: ContextVar[Optional[str]] = ContextVar("span_id", default=None)


class ElasticsearchHandler(logging.Handler):
    """Custom logging handler that sends logs to Elasticsearch."""

    def __init__(self, elasticsearch_url: str, index_name: str):
        super().__init__()
        self.elasticsearch_url = elasticsearch_url
        self.index_name = index_name
        self.es_client: Optional[Elasticsearch] = None
        self._initialize_client()

    def _initialize_client(self):
        """Initialize Elasticsearch client with error handling."""
        try:
            self.es_client = Elasticsearch([self.elasticsearch_url])
            # Test connection
            if self.es_client:
                self.es_client.info()
        except ESConnectionError:
            print(
                f"Warning: Could not connect to Elasticsearch at {self.elasticsearch_url}"
            )
            self.es_client = None
        except Exception as e:
            print(f"Warning: Elasticsearch initialization failed: {e}")
            self.es_client = None

    def emit(self, record):
        """Send log record to Elasticsearch."""
        if not self.es_client:
            return

        try:
            log_entry = {
                "@timestamp": record.created * 1000,  # Convert to milliseconds
                "level": record.levelname,
                "logger": record.name,
                "message": record.getMessage(),
                "service": settings.otel_service_name,
                "version": settings.otel_service_version,
            }

            # Add request context if available
            request_id = request_id_var.get()
            if request_id:
                log_entry["request_id"] = request_id

            trace_id = trace_id_var.get()
            if trace_id:
                log_entry["trace_id"] = trace_id

            span_id = span_id_var.get()
            if span_id:
                log_entry["span_id"] = span_id

            # Add exception info if present
            if record.exc_info:
                log_entry["exception"] = self.format(record)

            # Add extra fields from the record
            for key, value in record.__dict__.items():
                if key not in [
                    "name",
                    "msg",
                    "args",
                    "levelname",
                    "levelno",
                    "pathname",
                    "filename",
                    "module",
                    "exc_info",
                    "exc_text",
                    "stack_info",
                    "lineno",
                    "funcName",
                    "created",
                    "msecs",
                    "relativeCreated",
                    "thread",
                    "threadName",
                    "processName",
                    "process",
                    "message",
                ]:
                    log_entry[key] = value

            self.es_client.index(index=self.index_name, body=log_entry)
        except Exception as e:
            print(f"Failed to send log to Elasticsearch: {e}")


def add_trace_context(logger, method_name, event_dict):
    """Add OpenTelemetry trace context to log events."""
    span = trace.get_current_span()
    if span:
        span_context = span.get_span_context()
        if span_context.is_valid:
            event_dict["trace_id"] = format(span_context.trace_id, "032x")
            event_dict["span_id"] = format(span_context.span_id, "016x")

    # Add request ID if available
    request_id = request_id_var.get()
    if request_id:
        event_dict["request_id"] = request_id

    return event_dict


def setup_opentelemetry():
    """Initialize OpenTelemetry tracing and metrics."""
    if not settings.enable_tracing:
        return

    # Create resource with service information
    resource_attributes = {
        "service.name": settings.otel_service_name,
        "service.version": settings.otel_service_version,
        "service.namespace": "microservices",
    }

    # Add additional resource attributes from config
    if settings.otel_resource_attributes:
        for attr in settings.otel_resource_attributes.split(","):
            if "=" in attr:
                key, value = attr.split("=", 1)
                resource_attributes[key.strip()] = value.strip()

    resource = Resource.create(resource_attributes)

    # Setup tracing
    if settings.enable_tracing:
        trace.set_tracer_provider(TracerProvider(resource=resource))

        # Setup OTLP exporter
        headers = {}
        if settings.otel_exporter_otlp_headers:
            for header in settings.otel_exporter_otlp_headers.split(","):
                if "=" in header:
                    key, value = header.split("=", 1)
                    headers[key.strip()] = value.strip()

        otlp_exporter = OTLPSpanExporter(
            endpoint=f"{settings.otel_exporter_otlp_endpoint}/v1/traces",
            headers=headers,
        )

        span_processor = BatchSpanProcessor(otlp_exporter)
        tracer_provider = trace.get_tracer_provider()
        if hasattr(tracer_provider, "add_span_processor"):
            tracer_provider.add_span_processor(span_processor)  # type: ignore

    # Setup metrics
    if settings.enable_metrics:
        metric_reader = PeriodicExportingMetricReader(
            OTLPMetricExporter(
                endpoint=f"{settings.otel_exporter_otlp_endpoint}/v1/metrics",
                headers=headers if "headers" in locals() else {},
            ),
            export_interval_millis=10000,
        )
        metrics.set_meter_provider(
            MeterProvider(resource=resource, metric_readers=[metric_reader])
        )


def setup_instrumentation():
    """Setup OpenTelemetry auto-instrumentation."""
    if settings.enable_tracing:
        try:
            # Instrument FastAPI
            FastAPIInstrumentor().instrument()  # type: ignore

            # Instrument HTTP clients
            HTTPXClientInstrumentor().instrument()  # type: ignore
            RequestsInstrumentor().instrument()  # type: ignore

            # Instrument logging
            if settings.enable_logging:
                LoggingInstrumentor().instrument()  # type: ignore
        except Exception as e:
            print(f"Warning: Could not setup OpenTelemetry instrumentation: {e}")


def setup_logging():
    """Configure structured logging with ELK stack support."""
    # Configure structlog
    processors = [
        structlog.contextvars.merge_contextvars,
        structlog.processors.TimeStamper(fmt="ISO"),
        add_trace_context,
        structlog.processors.add_log_level,
        structlog.processors.StackInfoRenderer(),
        structlog.dev.set_exc_info,
    ]

    # Add JSON formatting for production, pretty formatting for development
    if settings.debug:
        processors.append(structlog.dev.ConsoleRenderer())  # type: ignore
    else:
        processors.append(structlog.processors.JSONRenderer())  # type: ignore

    structlog.configure(
        processors=processors,
        logger_factory=structlog.WriteLoggerFactory(),
        wrapper_class=structlog.make_filtering_bound_logger(
            getattr(logging, settings.log_level.upper())
        ),
        cache_logger_on_first_use=True,
    )

    # Configure standard logging
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=getattr(logging, settings.log_level.upper()),
    )

    # Add Elasticsearch handler if configured and not in debug mode
    if (
        settings.elasticsearch_url
        and not settings.debug
        and settings.elasticsearch_url.strip()  # Ensure URL is not empty
    ):
        try:
            es_handler = ElasticsearchHandler(
                settings.elasticsearch_url, settings.elasticsearch_index
            )
            es_handler.setLevel(getattr(logging, settings.log_level.upper()))
            logging.getLogger().addHandler(es_handler)
        except Exception as e:
            print(f"Warning: Could not add Elasticsearch handler: {e}")


def get_logger(name: Optional[str] = None):
    """Get a structured logger instance."""
    return structlog.get_logger(name or __name__)


def set_request_id(request_id: Optional[str] = None):
    """Set request ID in context for request tracing."""
    if request_id is None:
        request_id = str(uuid.uuid4())

    request_id_var.set(request_id)
    return request_id


def get_request_id() -> Optional[str]:
    """Get current request ID from context."""
    return request_id_var.get()


def initialize_observability():
    """Initialize all observability components."""
    setup_logging()
    setup_opentelemetry()
    setup_instrumentation()
