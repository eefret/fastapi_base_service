import time
import uuid
from typing import Callable
from fastapi import Request, Response
from fastapi.responses import JSONResponse
import structlog

logger = structlog.get_logger()


async def error_handler_middleware(request: Request, call_next: Callable) -> Response:
    request_id = str(uuid.uuid4())
    start_time = time.time()

    # Add request ID to structured logging context
    structlog.contextvars.clear_contextvars()
    structlog.contextvars.bind_contextvars(request_id=request_id)

    logger.info(
        "Request started",
        method=request.method,
        url=str(request.url),
        path=request.url.path,
    )

    try:
        response = await call_next(request)

        processing_time = time.time() - start_time

        logger.info(
            "Request completed",
            status_code=response.status_code,
            processing_time=processing_time,
        )

        # Add request ID to response headers
        response.headers["X-Request-ID"] = request_id
        return response

    except Exception as e:
        processing_time = time.time() - start_time

        logger.error(
            "Request failed",
            error=str(e),
            error_type=type(e).__name__,
            processing_time=processing_time,
        )

        return JSONResponse(
            status_code=500,
            content={
                "error": "Internal server error",
                "request_id": request_id,
                "message": str(e) if request.app.state.settings.debug else "Something went wrong",
            },
            headers={"X-Request-ID": request_id},
        )
