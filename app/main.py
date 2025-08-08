from datetime import datetime, timezone
from contextlib import asynccontextmanager
import structlog
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.dependencies import container, get_business_service
from app.models.requests import (
    HealthCheckResponse,
    ProcessDataRequest,
    ProcessDataResponse,
)
from app.services.business_service import BusinessService
from app.middleware.error_handler import error_handler_middleware


# Configure structured logging
import logging

structlog.configure(
    processors=[
        structlog.contextvars.merge_contextvars,
        structlog.processors.add_log_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.dev.ConsoleRenderer()
        if settings.debug
        else structlog.processors.JSONRenderer(),
    ],
    wrapper_class=structlog.make_filtering_bound_logger(
        getattr(logging, settings.log_level.upper(), logging.INFO)
    ),
    logger_factory=structlog.PrintLoggerFactory(),
    cache_logger_on_first_use=True,
)

logger = structlog.get_logger()


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    logger.info(
        "Starting up service", app_name=settings.app_name, version=settings.app_version
    )

    # Wire the dependency injection container
    container.wire(modules=[__name__])

    yield

    # Shutdown
    logger.info("Shutting down service")

    # Close HTTP client
    await container.http_client().aclose()


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="FastAPI microservice template with dependency injection",
    lifespan=lifespan,
)

# Store settings in app state for middleware access
app.state.settings = settings

# Middleware
app.middleware("http")(error_handler_middleware)

app.add_middleware(
    CORSMiddleware,  # type: ignore
    allow_origins=["*"],  # Configure appropriately for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health", response_model=HealthCheckResponse)
async def health_check() -> HealthCheckResponse:
    return HealthCheckResponse(
        status="healthy",
        version=settings.app_version,
        timestamp=datetime.now(timezone.utc).isoformat(),
    )


@app.post("/process", response_model=ProcessDataResponse)
async def process_data(
    request: ProcessDataRequest,
    business_service: BusinessService = Depends(get_business_service),
) -> ProcessDataResponse:
    try:
        result = await business_service.process_data(
            input_data=request.input_data,
            options=request.options,
        )

        return ProcessDataResponse(**result)

    except Exception as e:
        logger.error("Failed to process data", error=str(e))
        raise HTTPException(status_code=500, detail="Processing failed")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host=settings.host,
        port=settings.port,
        reload=settings.debug,
        log_level=settings.log_level.lower(),
    )
