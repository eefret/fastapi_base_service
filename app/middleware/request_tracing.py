"""
Request tracing middleware for OpenTelemetry and structured logging.
"""
import time
import uuid
from typing import Callable
from fastapi import Request, Response
from opentelemetry import trace

from app.observability import set_request_id, get_logger

logger = get_logger(__name__)


async def request_tracing_middleware(request: Request, call_next: Callable) -> Response:
    """
    Middleware to add request tracing and structured logging context.

    This middleware:
    1. Generates a unique request ID for each request
    2. Sets up tracing context
    3. Logs request/response information
    4. Measures request duration
    """
    # Generate unique request ID
    request_id = str(uuid.uuid4())
    set_request_id(request_id)

    # Start timing
    start_time = time.time()

    # Get trace information if available
    tracer = trace.get_tracer(__name__)

    with tracer.start_as_current_span(f"{request.method} {request.url.path}") as span:
        # Set span attributes
        span.set_attribute("http.method", request.method)
        span.set_attribute("http.url", str(request.url))
        span.set_attribute("http.scheme", request.url.scheme)
        span.set_attribute("http.host", request.url.hostname or "")
        span.set_attribute("http.target", request.url.path)
        span.set_attribute("request.id", request_id)

        # Log request start
        logger.info(
            "Request started",
            request_id=request_id,
            method=request.method,
            path=request.url.path,
            query_params=str(request.query_params) if request.query_params else None,
            client_ip=request.client.host if request.client else None,
            user_agent=request.headers.get("user-agent"),
        )

        try:
            # Process the request
            response = await call_next(request)

            # Calculate duration
            duration = time.time() - start_time

            # Set additional span attributes
            span.set_attribute("http.status_code", response.status_code)
            span.set_attribute(
                "http.response_size", response.headers.get("content-length", 0)
            )

            # Log successful request completion
            logger.info(
                "Request completed",
                request_id=request_id,
                method=request.method,
                path=request.url.path,
                status_code=response.status_code,
                duration_ms=round(duration * 1000, 2),
            )

            # Add request ID to response headers for client tracing
            response.headers["X-Request-ID"] = request_id

            return response

        except Exception as e:
            # Calculate duration
            duration = time.time() - start_time

            # Set error span attributes
            span.set_attribute("http.status_code", 500)
            span.record_exception(e)
            span.set_status(trace.Status(trace.StatusCode.ERROR, str(e)))

            # Log request error
            logger.error(
                "Request failed",
                request_id=request_id,
                method=request.method,
                path=request.url.path,
                duration_ms=round(duration * 1000, 2),
                error=str(e),
                exc_info=True,
            )

            # Re-raise the exception to be handled by error middleware
            raise
