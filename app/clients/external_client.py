from abc import ABC, abstractmethod
import httpx
import structlog

logger = structlog.get_logger()


class BaseClient(ABC):
    def __init__(self, http_client: httpx.AsyncClient, base_url: str):
        self.http_client = http_client
        self.base_url = base_url.rstrip("/")

    async def _make_request(
        self,
        method: str,
        endpoint: str,
        **kwargs
    ) -> dict:
        url = f"{self.base_url}{endpoint}"
        try:
            response = await self.http_client.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPError as e:
            logger.error(
                "HTTP request failed",
                url=url,
                method=method,
                error=str(e)
            )
            raise


class ExternalServiceAClient(BaseClient):
    async def get_data(self, query: str) -> dict:
        return await self._make_request(
            "GET",
            "/api/data",
            params={"query": query}
        )

    async def process_item(self, item_data: dict) -> dict:
        return await self._make_request(
            "POST",
            "/api/process",
            json=item_data
        )


class ExternalServiceBClient(BaseClient):
    async def fetch_metadata(self, item_id: str) -> dict:
        return await self._make_request(
            "GET",
            f"/api/items/{item_id}/metadata"
        )

    async def update_status(self, item_id: str, status: str) -> dict:
        return await self._make_request(
            "PATCH",
            f"/api/items/{item_id}",
            json={"status": status}
        )
