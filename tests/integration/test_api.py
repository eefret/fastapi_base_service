from fastapi.testclient import TestClient


def test_health_check(test_client: TestClient):
    """Test health check endpoint."""
    response = test_client.get("/health")

    assert response.status_code == 200
    data = response.json()

    assert data["status"] == "healthy"
    assert "version" in data
    assert "timestamp" in data


def test_process_data_success(test_client: TestClient):
    """Test process data endpoint works."""
    # Act
    response = test_client.post(
        "/process", json={"input_data": "test_input", "options": {"key": "value"}}
    )

    # Assert
    assert response.status_code == 200
    data = response.json()

    # Check that all required fields are present
    assert "processed_data" in data
    assert "source_a_data" in data
    assert "source_b_data" in data
    assert "processing_time_ms" in data
    assert isinstance(data["processing_time_ms"], float)


def test_process_data_validation_error(test_client: TestClient):
    """Test process data endpoint with invalid input."""
    response = test_client.post("/process", json={"invalid_field": "test_input"})

    assert response.status_code == 422  # Validation error


def test_process_data_business_service_error(test_client: TestClient, monkeypatch):
    """Test process data endpoint when business service fails."""

    # Arrange - mock the business service to fail
    def mock_failing_process_data(*args, **kwargs):
        raise Exception("Business logic failed")

    from app.services import business_service

    monkeypatch.setattr(
        business_service.BusinessService, "process_data", mock_failing_process_data
    )

    # Act
    response = test_client.post(
        "/process", json={"input_data": "test_input", "options": {}}
    )

    # Assert
    assert response.status_code == 500
    data = response.json()
    assert data["detail"] == "Processing failed"
