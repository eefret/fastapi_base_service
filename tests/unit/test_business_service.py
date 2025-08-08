import pytest

from app.services.business_service import BusinessService


@pytest.mark.asyncio
async def test_process_data_success(
    mock_external_service_a_client,
    mock_external_service_b_client,
):
    """Test successful data processing with mocked external services."""
    # Arrange
    business_service = BusinessService(
        service_a_client=mock_external_service_a_client,
        service_b_client=mock_external_service_b_client,
    )

    input_data = "test_input"
    options = {"option1": "value1"}

    mock_external_service_a_client.get_data.return_value = {"result": "data_from_a"}
    mock_external_service_b_client.fetch_metadata.return_value = {"meta": "data_from_b"}

    # Act
    result = await business_service.process_data(input_data, options)

    # Assert
    assert "processed_data" in result
    assert "source_a_data" in result
    assert "source_b_data" in result
    assert "processing_time_ms" in result
    assert isinstance(result["processing_time_ms"], float)

    # Verify external service calls
    mock_external_service_a_client.get_data.assert_called_once_with(input_data)
    mock_external_service_b_client.fetch_metadata.assert_called_once_with(input_data)


@pytest.mark.asyncio
async def test_process_data_with_service_a_failure(
    mock_external_service_a_client,
    mock_external_service_b_client,
):
    """Test data processing when Service A fails."""
    # Arrange
    business_service = BusinessService(
        service_a_client=mock_external_service_a_client,
        service_b_client=mock_external_service_b_client,
    )

    input_data = "test_input"
    options = {}

    # Simulate Service A failure
    mock_external_service_a_client.get_data.side_effect = Exception(
        "Service A unavailable"
    )
    mock_external_service_b_client.fetch_metadata.return_value = {"meta": "data_from_b"}

    # Act
    result = await business_service.process_data(input_data, options)

    # Assert
    assert "processed_data" in result
    assert "source_a_data" in result
    assert "source_b_data" in result

    # Service A should return empty dict due to exception
    assert result["source_a_data"] == "{}"
    # Service B should work normally
    assert "data_from_b" in result["source_b_data"]


@pytest.mark.asyncio
async def test_process_data_with_both_services_failing(
    mock_external_service_a_client,
    mock_external_service_b_client,
):
    """Test data processing when both external services fail."""
    # Arrange
    business_service = BusinessService(
        service_a_client=mock_external_service_a_client,
        service_b_client=mock_external_service_b_client,
    )

    input_data = "test_input"
    options = {}

    # Simulate both services failing
    mock_external_service_a_client.get_data.side_effect = Exception(
        "Service A unavailable"
    )
    mock_external_service_b_client.fetch_metadata.side_effect = Exception(
        "Service B unavailable"
    )

    # Act
    result = await business_service.process_data(input_data, options)

    # Assert
    assert "processed_data" in result
    assert result["source_a_data"] == "{}"
    assert result["source_b_data"] == "{}"

    # Business logic should still work with empty data
    assert "Processed:" in result["processed_data"]
