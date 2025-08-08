from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    # Application settings
    app_name: str = Field(
        default="FastAPI Base Service", description="Application name"
    )
    app_version: str = Field(default="0.1.0", description="Application version")
    debug: bool = Field(default=False, description="Debug mode")

    # Server settings
    host: str = Field(default="0.0.0.0", description="Server host")
    port: int = Field(default=8000, description="Server port")

    # External service URLs (examples)
    external_service_a_url: str = Field(
        default="", description="External service A base URL"
    )
    external_service_b_url: str = Field(
        default="", description="External service B base URL"
    )

    # HTTP client settings
    http_timeout: float = Field(
        default=30.0, description="HTTP request timeout in seconds"
    )
    http_retries: int = Field(default=3, description="Number of HTTP request retries")

    # Logging settings
    log_level: str = Field(default="INFO", description="Logging level")

    # ELK Stack settings
    elasticsearch_url: str = Field(
        default="http://localhost:9200", description="Elasticsearch URL"
    )
    elasticsearch_index: str = Field(
        default="fastapi-logs", description="Elasticsearch index for logs"
    )

    # OpenTelemetry settings
    otel_service_name: str = Field(
        default="fastapi-base-service", description="OpenTelemetry service name"
    )
    otel_service_version: str = Field(
        default="0.1.0", description="OpenTelemetry service version"
    )
    otel_exporter_otlp_endpoint: str = Field(
        default="http://localhost:4318", description="OTLP exporter endpoint"
    )
    otel_exporter_otlp_headers: str = Field(
        default="", description="OTLP exporter headers (key1=value1,key2=value2)"
    )
    otel_resource_attributes: str = Field(
        default="", description="Additional resource attributes"
    )
    enable_tracing: bool = Field(
        default=True, description="Enable OpenTelemetry tracing"
    )
    enable_metrics: bool = Field(
        default=True, description="Enable OpenTelemetry metrics"
    )
    enable_logging: bool = Field(
        default=True, description="Enable OpenTelemetry logging"
    )


settings = Settings()
