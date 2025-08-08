import pytest
import pytest_asyncio
from unittest.mock import AsyncMock
from fastapi.testclient import TestClient
import httpx

from app.main import app
from app.clients.external_client import ExternalServiceAClient, ExternalServiceBClient
from app.services.business_service import BusinessService


@pytest.fixture
def test_client():
    """Create a test client for FastAPI app."""
    return TestClient(app)


@pytest_asyncio.fixture
async def mock_http_client():
    """Create a mock HTTP client."""
    client = AsyncMock(spec=httpx.AsyncClient)
    return client


@pytest_asyncio.fixture
async def mock_external_service_a_client():
    """Create a mock for External Service A client."""
    client = AsyncMock(spec=ExternalServiceAClient)
    client.get_data = AsyncMock(return_value={"data": "service_a_data"})
    client.process_item = AsyncMock(return_value={"result": "processed"})
    return client


@pytest_asyncio.fixture
async def mock_external_service_b_client():
    """Create a mock for External Service B client."""
    client = AsyncMock(spec=ExternalServiceBClient)
    client.fetch_metadata = AsyncMock(return_value={"metadata": "service_b_metadata"})
    client.update_status = AsyncMock(return_value={"status": "updated"})
    return client


@pytest_asyncio.fixture
async def business_service_with_mocks(
    mock_external_service_a_client, mock_external_service_b_client
):
    """Create a BusinessService with mocked dependencies."""
    return BusinessService(
        service_a_client=mock_external_service_a_client,
        service_b_client=mock_external_service_b_client,
    )


@pytest.fixture
def override_dependencies():
    """Fixture to override FastAPI dependencies for testing."""

    def _override(overrides: dict):
        for dependency, mock in overrides.items():
            app.dependency_overrides[dependency] = lambda m=mock: m

    yield _override

    # Clean up overrides after test
    app.dependency_overrides.clear()
