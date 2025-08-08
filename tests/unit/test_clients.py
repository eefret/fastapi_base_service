import pytest
from unittest.mock import AsyncMock, MagicMock
import httpx

from app.clients.external_client import ExternalServiceAClient, ExternalServiceBClient


@pytest.mark.asyncio
async def test_external_service_a_get_data():
    """Test ExternalServiceAClient.get_data method."""
    # Arrange
    mock_http_client = AsyncMock(spec=httpx.AsyncClient)
    mock_response = MagicMock()
    mock_response.json.return_value = {"result": "test_data"}
    mock_response.raise_for_status.return_value = None
    mock_http_client.request.return_value = mock_response

    client = ExternalServiceAClient(
        http_client=mock_http_client, base_url="https://service-a.example.com"
    )

    # Act
    result = await client.get_data("test_query")

    # Assert
    assert result == {"result": "test_data"}
    mock_http_client.request.assert_called_once_with(
        "GET", "https://service-a.example.com/api/data", params={"query": "test_query"}
    )


@pytest.mark.asyncio
async def test_external_service_a_process_item():
    """Test ExternalServiceAClient.process_item method."""
    # Arrange
    mock_http_client = AsyncMock(spec=httpx.AsyncClient)
    mock_response = MagicMock()
    mock_response.json.return_value = {"processed": True}
    mock_response.raise_for_status.return_value = None
    mock_http_client.request.return_value = mock_response

    client = ExternalServiceAClient(
        http_client=mock_http_client, base_url="https://service-a.example.com"
    )

    item_data = {"item": "test_item"}

    # Act
    result = await client.process_item(item_data)

    # Assert
    assert result == {"processed": True}
    mock_http_client.request.assert_called_once_with(
        "POST", "https://service-a.example.com/api/process", json=item_data
    )


@pytest.mark.asyncio
async def test_external_service_b_fetch_metadata():
    """Test ExternalServiceBClient.fetch_metadata method."""
    # Arrange
    mock_http_client = AsyncMock(spec=httpx.AsyncClient)
    mock_response = MagicMock()
    mock_response.json.return_value = {"metadata": "test_metadata"}
    mock_response.raise_for_status.return_value = None
    mock_http_client.request.return_value = mock_response

    client = ExternalServiceBClient(
        http_client=mock_http_client, base_url="https://service-b.example.com"
    )

    # Act
    result = await client.fetch_metadata("item123")

    # Assert
    assert result == {"metadata": "test_metadata"}
    mock_http_client.request.assert_called_once_with(
        "GET", "https://service-b.example.com/api/items/item123/metadata"
    )


@pytest.mark.asyncio
async def test_client_http_error_handling():
    """Test client error handling when HTTP request fails."""
    # Arrange
    mock_http_client = AsyncMock(spec=httpx.AsyncClient)
    mock_http_client.request.side_effect = httpx.HTTPError("Connection failed")

    client = ExternalServiceAClient(
        http_client=mock_http_client, base_url="https://service-a.example.com"
    )

    # Act & Assert
    with pytest.raises(httpx.HTTPError):
        await client.get_data("test_query")
