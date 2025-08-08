from pydantic import BaseModel, Field


class HealthCheckResponse(BaseModel):
    status: str = Field(description="Service status")
    version: str = Field(description="Service version")
    timestamp: str = Field(description="Current timestamp")


class ProcessDataRequest(BaseModel):
    input_data: str = Field(description="Input data to process")
    options: dict[str, str] = Field(default_factory=dict, description="Processing options")


class ProcessDataResponse(BaseModel):
    processed_data: str = Field(description="Processed result")
    source_a_data: str = Field(description="Data from external service A")
    source_b_data: str = Field(description="Data from external service B")
    processing_time_ms: float = Field(description="Processing time in milliseconds")
