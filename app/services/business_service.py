import asyncio
import time
import structlog
from typing import Tuple, cast

from app.clients.external_client import ExternalServiceAClient, ExternalServiceBClient

logger = structlog.get_logger()


class BusinessService:
    def __init__(
        self,
        service_a_client: ExternalServiceAClient,
        service_b_client: ExternalServiceBClient,
    ):
        self.service_a_client = service_a_client
        self.service_b_client = service_b_client

    async def process_data(self, input_data: str, options: dict[str, str]) -> dict:
        start_time = time.time()

        logger.info("Starting data processing", input_data=input_data, options=options)

        # Call both external services concurrently
        service_a_data, service_b_data = await self._fetch_external_data(input_data)

        # Business logic - combine and process the data
        processed_result = self._combine_data(
            input_data, service_a_data, service_b_data
        )

        processing_time = (time.time() - start_time) * 1000

        logger.info("Data processing completed", processing_time_ms=processing_time)

        return {
            "processed_data": processed_result,
            "source_a_data": str(service_a_data),
            "source_b_data": str(service_b_data),
            "processing_time_ms": processing_time,
        }

    async def _fetch_external_data(self, input_data: str) -> Tuple[dict, dict]:
        """Fetch data from both external services concurrently."""
        tasks = [
            self.service_a_client.get_data(input_data),
            self.service_b_client.fetch_metadata(input_data),
        ]

        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Handle exceptions
        service_a_result = results[0]
        service_a_data: dict = (
            cast(dict, service_a_result)
            if not isinstance(service_a_result, Exception)
            else {}
        )

        service_b_data: dict = {}
        if len(results) > 1:
            service_b_result = results[1]
            service_b_data = (
                cast(dict, service_b_result)
                if not isinstance(service_b_result, Exception)
                else {}
            )

        if isinstance(service_a_result, Exception):
            logger.warning("Service A call failed", error=str(service_a_result))

        if len(results) > 1 and isinstance(results[1], Exception):
            logger.warning("Service B call failed", error=str(results[1]))

        return service_a_data, service_b_data

    def _combine_data(
        self, input_data: str, service_a_data: dict, service_b_data: dict
    ) -> str:
        """Business logic to combine data from different sources."""
        combined = {
            "input": input_data,
            "enriched_a": service_a_data,
            "enriched_b": service_b_data,
            "processed_at": time.time(),
        }

        # Example business logic - you'd replace this with actual processing
        return f"Processed: {len(str(combined))} characters of data"
