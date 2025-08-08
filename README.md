# FastAPI Microservice Template

[![CI](https://github.com/eefret/fastapi_base_service/workflows/CI/badge.svg)](https://github.com/eefret/fastapi_base_service/actions)
[![codecov](https://codecov.io/gh/eefret/fastapi_base_service/branch/main/graph/badge.svg)](https://codecov.io/gh/eefret/fastapi_base_service)
[![Python](https://img.shields.io/badge/python-3.12%20|%203.13-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-00a393.svg?style=flat&logo=FastAPI&logoColor=white)](https://fastapi.tiangolo.com/)
[![UV](https://img.shields.io/badge/packaged%20with-uv-de5fe4?style=flat&logo=uv&logoColor=white)](https://github.com/astral-sh/uv)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A comprehensive, production-ready FastAPI microservice template designed for developers to build robust, testable microservices with external API integrations.

Made with ❤️ by [Chris](https://github.com/eefret) for my muse [Ana](https://github.com/LlanoAna)

## 🎯 What This Template Provides

This template gives you everything needed to build a microservice that:
- Receives HTTP requests
- Calls multiple external APIs
- Processes and combines data
- Returns structured responses
- Is fully testable with mocked dependencies
- Is ready for production deployment

## 🛠️ Technology Stack & Why We Chose Each Library

### Core Framework
- **FastAPI** - Modern, fast Python web framework chosen for:
  - Automatic API documentation (OpenAPI/Swagger)
  - Built-in data validation with Pydantic
  - Native async/await support
  - Excellent type hints integration
  - High performance (comparable to NodeJS and Go)

### Development Tools
- **UV** - Ultra-fast Python package manager chosen for:
  - 10-100x faster than pip for dependency resolution
  - Built-in virtual environment management
  - Better dependency locking and reproducible builds
  - Modern replacement for pip-tools and virtualenv

- **pyrefly** - Ultra-fast Python type checker chosen over PyRight/mypy because:
  - Written in Rust for maximum performance (10x+ faster than PyRight)
  - Extremely fast incremental type checking
  - Modern architecture designed for speed
  - Compatible with existing Python type hints
  - Better developer experience with faster feedback loops

### Web Server & HTTP
- **uvicorn** - Lightning-fast ASGI server chosen for:
  - Excellent performance with async Python code
  - Built-in support for FastAPI features
  - Auto-reload during development
  - Production-ready with proper process management

- **httpx** - Modern HTTP client chosen over requests because:
  - Native async/await support (crucial for performance)
  - HTTP/2 support
  - Streaming responses
  - Same API as requests but async-first

### Architecture & Design Patterns
- **dependency-injector** - Professional DI framework chosen for:
  - Clean separation of concerns
  - Easy testing with mock injection
  - Configuration management
  - Lazy loading of dependencies
  - Better than manual dependency management

- **pydantic** - Data validation library chosen for:
  - Runtime type checking and validation
  - Automatic serialization/deserialization
  - Clear error messages for invalid data
  - Seamless integration with FastAPI
  - Settings management with environment variables

### Testing & Quality
- **pytest** - De facto standard Python testing framework chosen for:
  - Simple, readable test syntax
  - Powerful fixtures system
  - Excellent plugin ecosystem
  - Async test support
  - Better than unittest for modern Python

- **pytest-mock** - Mocking utilities chosen because:
  - Cleaner syntax than raw unittest.mock
  - Automatic cleanup of mocks
  - Better integration with pytest fixtures
  - AsyncMock support for async functions

- **ruff** - Ultra-fast Python linter and formatter chosen for:
  - Written in Rust for maximum performance (10-100x faster than flake8)
  - All-in-one tool combining linting and formatting
  - Compatible with existing Python tools and rules
  - Modern replacement for flake8, black, and other tools

### Logging & Observability
- **structlog** - Structured logging chosen over standard logging because:
  - JSON output for better log parsing
  - Context variables for request tracing
  - Better performance than standard logging
  - More readable logs during development
  - Essential for microservices observability

### Containerization
- **Docker** - Industry standard containerization chosen for:
  - Consistent environments across dev/staging/prod
  - Easy deployment to any cloud provider
  - Isolation and security
  - Scalability with container orchestrators

## 🚀 Quick Start Guide

### Prerequisites

- Python 3.12 or higher
- [UV package manager](https://github.com/astral-sh/uv) installed
- Docker (optional, for containerization)

### 1. Clone and Setup

```bash
# Clone the repository
git clone <your-repo-url>
cd fastapi_base_service

# Install UV package manager (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install all dependencies (including development tools)
make dev-install

# Copy the example environment file
cp .env.example .env

# (Optional) Set up pre-commit hooks for code quality
make pre-commit-install
```

### 2. Configure Your Service

Edit the `.env` file with your service details:

```env
# Your service information
APP_NAME="My Amazing Microservice"
APP_VERSION="1.0.0"
DEBUG=true

# Server settings
HOST=0.0.0.0
PORT=8000

# External APIs your service will call
EXTERNAL_SERVICE_A_URL=https://api.example-service-a.com
EXTERNAL_SERVICE_B_URL=https://api.example-service-b.com

# HTTP client settings
HTTP_TIMEOUT=30.0
HTTP_RETRIES=3

# Logging
LOG_LEVEL=INFO
```

### 3. Customize Service Name (Optional)

```bash
# Change the service name from the default "fastapi-base-service"
make change-name name=my-awesome-service

# This updates:
# - pyproject.toml package name
# - .env.example APP_NAME
# - GitHub Actions workflow
# - Docker image name
```

### 4. Run Your Service

```bash
# Start in development mode (auto-reloads on code changes)
make dev

# Your service is now running at http://localhost:8000
# Open API documentation in browser (in another terminal)
make docs
```

### 5. Test Everything Works

```bash
# Check health endpoint
curl http://localhost:8000/health

# Test the main endpoint
curl -X POST "http://localhost:8000/process" \
     -H "Content-Type: application/json" \
     -d '{"input_data": "hello world", "options": {"test": "true"}}'
```

## 📚 API Documentation

FastAPI automatically generates interactive API documentation that you can access while your service is running:

### Built-in Documentation
```bash
# Start your service
make dev

# Open interactive API docs (in another terminal)
make docs
```

**Available documentation endpoints:**
- **Swagger UI**: `http://localhost:8000/docs` (interactive, test APIs directly)
- **ReDoc**: `http://localhost:8000/redoc` (clean, printable documentation)
- **OpenAPI JSON**: `http://localhost:8000/openapi.json` (machine-readable API spec)

### Default API Endpoints

- `GET /health` - Health check endpoint
- `POST /process` - Main data processing endpoint

**Try it interactively:**
1. Run `make dev` to start your service
2. Run `make docs` to open the interactive documentation
3. Click on any endpoint to see details and test it directly in the browser!

## 📁 Project Structure Explained

```
fastapi_base_service/
├── app/                          # Main application code
│   ├── main.py                   # FastAPI app setup and routes
│   ├── config.py                 # Configuration management
│   ├── dependencies.py           # Dependency injection setup
│   ├── observability.py          # OpenTelemetry and logging setup
│   ├── clients/                  # External service clients
│   │   └── external_client.py    # HTTP client classes
│   ├── services/                 # Business logic
│   │   └── business_service.py   # Main business logic
│   ├── models/                   # Data models
│   │   └── requests.py           # Request/response models
│   └── middleware/               # Custom middleware
│       ├── error_handler.py      # Error handling
│       └── request_tracing.py    # Request tracing and correlation
├── tests/                        # All tests
│   ├── conftest.py              # Test configuration and fixtures
│   ├── unit/                    # Unit tests
│   └── integration/             # API integration tests
├── k8s/                         # Kubernetes deployment files
│   ├── configs/                 # Configuration files for services
│   │   ├── logstash/           # Logstash pipeline and config
│   │   │   ├── config/
│   │   │   └── pipeline/
│   │   └── otel-collector/     # OpenTelemetry Collector config
│   │       └── config.yml
│   ├── elasticsearch.yml       # Elasticsearch deployment
│   ├── fastapi-app.yml         # FastAPI application deployment
│   ├── kibana.yml              # Kibana deployment
│   ├── otel-collector.yml      # OpenTelemetry Collector deployment
│   ├── namespace.yml           # Kubernetes namespace
│   ├── setup-minikube.sh       # Automated Minikube setup
│   └── README.md               # Deployment instructions
├── docker-compose.elk.yml       # ELK stack for development
├── docker-compose.simple.yml    # Simple FastAPI setup
├── .env.example                 # Environment variables template
├── pyproject.toml              # Dependencies and tool configuration
├── Makefile                    # Development commands
└── Dockerfile                  # Container configuration
```

## 🏛️ Architecture Deep Dive

### Overall Architecture Pattern

This template implements a **Clean Architecture** pattern with **Dependency Injection**, specifically designed for microservices that integrate with external APIs. Here's how the layers work:

```
┌─────────────────────────────────────────────────────────────┐
│                    HTTP Layer (FastAPI)                     │
│  ┌─────────────────┐  ┌──────────────────┐  ┌─────────────┐ │
│  │   Middleware    │  │   API Routes     │  │ Validation  │ │
│  │ (Error, CORS,   │  │  (main.py)       │  │ (Pydantic)  │ │
│  │  Logging)       │  │                  │  │             │ │
│  └─────────────────┘  └──────────────────┘  └─────────────┘ │
└─────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                   Business Logic Layer                      │
│  ┌───────────────────────────────────────────────────────┐  │
│  │              Business Services                        │  │
│  │         (services/business_service.py)                │  │
│  │  • Orchestrates multiple external calls               │  │
│  │  • Implements business logic                          │  │
│  │  • Handles failures gracefully                        │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                   External Integration Layer                │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────┐  │
│  │  Service A      │  │  Service B      │  │  Service N  │  │
│  │  Client         │  │  Client         │  │  Client     │  │
│  │ (HTTP Calls)    │  │ (HTTP Calls)    │  │ (HTTP Calls)│  │
│  └─────────────────┘  └─────────────────┘  └─────────────┘  │
└─────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                     External APIs                           │
│   🌐 External Service A    🌐 External Service B           │
└─────────────────────────────────────────────────────────────┘
```

### Key Architectural Decisions

#### 1. **Dependency Injection Container**
- **Why**: Makes testing easy by allowing mock injection
- **How**: `dependency-injector` manages all dependencies
- **Benefits**:
  - Easy to test (inject mocks)
  - Loose coupling between components
  - Configuration centralized
  - Lazy loading of expensive resources

#### 2. **Async-First Design**
- **Why**: Microservices often wait on external APIs
- **How**: All I/O operations use async/await
- **Benefits**:
  - High concurrency with low memory usage
  - Can handle many requests simultaneously
  - Perfect for I/O-bound workloads (most microservices)

#### 3. **Client Abstraction Layer**
- **Why**: Isolates external API complexity
- **How**: Base client class with common HTTP functionality
- **Benefits**:
  - Consistent error handling
  - Easy to mock for testing
  - Centralized logging and retry logic
  - Can swap implementations easily

#### 4. **Structured Logging with Request Tracing**
- **Why**: Essential for debugging distributed systems
- **How**: Each request gets unique ID, structured JSON logs
- **Benefits**:
  - Easy to trace requests across services
  - Searchable logs in production
  - Context preservation across async calls

### Data Flow Example

Here's what happens when a request comes in:

```python
# 1. Request hits FastAPI endpoint
@app.post("/process")
async def process_data(request: ProcessDataRequest, service = Depends(get_business_service)):

    # 2. Request is validated by Pydantic
    # 3. Dependency injection provides business service
    # 4. Business service orchestrates external calls

    result = await business_service.process_data(request.input_data, request.options)
    return ProcessDataResponse(**result)

# Inside BusinessService.process_data():
async def process_data(self, input_data: str, options: dict):
    # 5. Multiple external services called concurrently
    service_a_data, service_b_data = await asyncio.gather(
        self.service_a_client.get_data(input_data),      # Concurrent call 1
        self.service_b_client.fetch_metadata(input_data)  # Concurrent call 2
    )

    # 6. Business logic combines results
    processed_result = self._combine_data(input_data, service_a_data, service_b_data)

    # 7. Structured response returned
    return {
        "processed_data": processed_result,
        "source_a_data": str(service_a_data),
        "source_b_data": str(service_b_data),
        "processing_time_ms": processing_time
    }
```

### Why This Architecture Works for Microservices

1. **Testability**: Every dependency is injected and mockable
2. **Scalability**: Async design handles high concurrency
3. **Maintainability**: Clear separation of concerns
4. **Observability**: Structured logging and error handling
5. **Resilience**: Graceful handling of external service failures
6. **Developer Experience**: Type safety and auto-completion everywhere

### Testing Architecture

The testing strategy mirrors the application architecture:

```
Unit Tests (tests/unit/)
├── test_business_service.py     # Tests business logic with mocked clients
├── test_clients.py              # Tests HTTP clients with mocked httpx
└── test_*.py                    # Other unit tests

Integration Tests (tests/integration/)
├── test_api.py                  # Tests FastAPI endpoints with mocked services
└── test_*.py                    # Other integration tests

Test Configuration (tests/conftest.py)
├── Mock fixtures for all external dependencies
├── Test client configuration
└── Shared test utilities
```

This architecture ensures that:
- **Unit tests** are fast (no external calls)
- **Integration tests** verify the API contract
- **All external dependencies are mockable**
- **Tests are isolated and predictable**

## 🏗️ How to Build Your Own Microservice

Follow this step-by-step guide to transform this template into your own microservice.

### Step 1: Define Your Data Models

Start by defining what data your service will receive and return.

**Example: Building a User Profile Service**

Edit `app/models/requests.py`:

```python
from pydantic import BaseModel, Field
from typing import Optional

class UserProfileRequest(BaseModel):
    user_id: str = Field(description="User ID to fetch profile for")
    include_preferences: bool = Field(default=True, description="Include user preferences")
    include_history: bool = Field(default=False, description="Include user history")

class UserProfileResponse(BaseModel):
    user_id: str = Field(description="User ID")
    name: str = Field(description="User's full name")
    email: str = Field(description="User's email")
    preferences: Optional[dict] = Field(default=None, description="User preferences")
    history: Optional[list] = Field(default=None, description="User history")
    last_updated: str = Field(description="Last update timestamp")
```

### Step 2: Create External Service Clients

Define the external APIs your service will call.

**Example: User Service and Analytics Service clients**

Edit `app/clients/external_client.py` and add your clients:

```python
class UserServiceClient(BaseClient):
    """Client for the User Management Service"""

    async def get_user_details(self, user_id: str) -> dict:
        """Fetch basic user information"""
        return await self._make_request(
            "GET",
            f"/api/v1/users/{user_id}"
        )

    async def get_user_preferences(self, user_id: str) -> dict:
        """Fetch user preferences"""
        return await self._make_request(
            "GET",
            f"/api/v1/users/{user_id}/preferences"
        )

class AnalyticsServiceClient(BaseClient):
    """Client for the Analytics Service"""

    async def get_user_history(self, user_id: str, limit: int = 10) -> dict:
        """Fetch user activity history"""
        return await self._make_request(
            "GET",
            f"/api/v1/analytics/users/{user_id}/history",
            params={"limit": limit}
        )
```

### Step 3: Update Configuration

Add your new external service URLs to `app/config.py`:

```python
class Settings(BaseSettings):
    # ... existing settings ...

    # Your external service URLs
    user_service_url: str = Field(default="", description="User Service base URL")
    analytics_service_url: str = Field(default="", description="Analytics Service base URL")
```

And update your `.env` file:

```env
USER_SERVICE_URL=https://api.userservice.com
ANALYTICS_SERVICE_URL=https://api.analytics.com
```

### Step 4: Update Dependency Injection

Register your new clients in `app/dependencies.py`:

```python
from app.clients.external_client import UserServiceClient, AnalyticsServiceClient
from app.services.user_profile_service import UserProfileService

class Container(containers.DeclarativeContainer):
    # ... existing providers ...

    # Your new service clients
    user_service_client = providers.Factory(
        UserServiceClient,
        http_client=http_client,
        base_url=settings.user_service_url,
    )

    analytics_service_client = providers.Factory(
        AnalyticsServiceClient,
        http_client=http_client,
        base_url=settings.analytics_service_url,
    )

    # Your business service
    user_profile_service = providers.Factory(
        UserProfileService,
        user_client=user_service_client,
        analytics_client=analytics_service_client,
    )

# Dependency functions for FastAPI
def get_user_profile_service() -> UserProfileService:
    return container.user_profile_service()
```

### Step 5: Implement Business Logic

Create your business service. Replace `app/services/business_service.py` or create a new file:

```python
# app/services/user_profile_service.py
import asyncio
import time
from datetime import datetime
import structlog

from app.clients.external_client import UserServiceClient, AnalyticsServiceClient

logger = structlog.get_logger()

class UserProfileService:
    def __init__(
        self,
        user_client: UserServiceClient,
        analytics_client: AnalyticsServiceClient,
    ):
        self.user_client = user_client
        self.analytics_client = analytics_client

    async def get_user_profile(
        self,
        user_id: str,
        include_preferences: bool = True,
        include_history: bool = False
    ) -> dict:
        """Get complete user profile from multiple services"""

        logger.info("Fetching user profile", user_id=user_id)

        # Always fetch basic user details
        tasks = [self.user_client.get_user_details(user_id)]

        # Conditionally fetch additional data
        if include_preferences:
            tasks.append(self.user_client.get_user_preferences(user_id))

        if include_history:
            tasks.append(self.analytics_client.get_user_history(user_id))

        # Execute all requests concurrently
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Process results
        user_details = results[0] if not isinstance(results[0], Exception) else {}

        preferences = None
        if include_preferences and len(results) > 1:
            preferences = results[1] if not isinstance(results[1], Exception) else None

        history = None
        if include_history:
            history_index = 2 if include_preferences else 1
            if len(results) > history_index:
                history = results[history_index] if not isinstance(results[history_index], Exception) else None

        # Combine all data
        return {
            "user_id": user_id,
            "name": user_details.get("name", "Unknown"),
            "email": user_details.get("email", ""),
            "preferences": preferences,
            "history": history,
            "last_updated": datetime.utcnow().isoformat(),
        }
```

### Step 6: Create API Endpoints

Update `app/main.py` to add your new endpoints:

```python
from app.models.requests import UserProfileRequest, UserProfileResponse
from app.services.user_profile_service import UserProfileService
from app.dependencies import get_user_profile_service

# Add this to your FastAPI app
@app.post("/user-profile", response_model=UserProfileResponse)
async def get_user_profile(
    request: UserProfileRequest,
    profile_service: UserProfileService = Depends(get_user_profile_service),
) -> UserProfileResponse:
    """Get comprehensive user profile"""
    try:
        result = await profile_service.get_user_profile(
            user_id=request.user_id,
            include_preferences=request.include_preferences,
            include_history=request.include_history,
        )

        return UserProfileResponse(**result)

    except Exception as e:
        logger.error("Failed to fetch user profile", error=str(e), user_id=request.user_id)
        raise HTTPException(status_code=500, detail="Profile fetch failed")
```

### Step 7: Write Tests

Create tests for your new service. The template provides comprehensive examples.

**Example: Testing your User Profile Service**

```python
# tests/unit/test_user_profile_service.py
import pytest
from unittest.mock import AsyncMock

from app.services.user_profile_service import UserProfileService

@pytest.mark.asyncio
async def test_get_user_profile_success():
    """Test successful user profile fetch"""
    # Arrange
    mock_user_client = AsyncMock()
    mock_analytics_client = AsyncMock()

    mock_user_client.get_user_details.return_value = {
        "name": "John Doe",
        "email": "john@example.com"
    }
    mock_user_client.get_user_preferences.return_value = {
        "theme": "dark",
        "notifications": True
    }

    service = UserProfileService(
        user_client=mock_user_client,
        analytics_client=mock_analytics_client
    )

    # Act
    result = await service.get_user_profile("user123")

    # Assert
    assert result["user_id"] == "user123"
    assert result["name"] == "John Doe"
    assert result["email"] == "john@example.com"
    assert result["preferences"]["theme"] == "dark"

    # Verify external calls were made
    mock_user_client.get_user_details.assert_called_once_with("user123")
    mock_user_client.get_user_preferences.assert_called_once_with("user123")
```

## 🧪 Testing Your Microservice

### Understanding the Mocking Strategy

The template uses **pytest-mock** and **unittest.mock** for mocking:

- **`AsyncMock`** - For mocking async functions and HTTP clients
- **`MagicMock`** - For mocking synchronous functions
- **`pytest-mock`** - Provides convenient fixtures and utilities

### Running Tests

```bash
# Run all tests
make test

# Run with coverage report
make test-cov

# Run specific test file
uv run pytest tests/unit/test_user_profile_service.py -v

# Run tests with detailed output
uv run pytest tests/ -v -s
```

### Test Structure

The template provides three types of tests:

1. **Unit Tests** (`tests/unit/`) - Test individual components with mocked dependencies
2. **Integration Tests** (`tests/integration/`) - Test API endpoints with mocked services
3. **Test Fixtures** (`tests/conftest.py`) - Reusable mock objects and configuration

### Example: Mocking External Services

```python
@pytest.fixture
async def mock_user_service_client():
    """Mock for user service client"""
    client = AsyncMock()
    client.get_user_details = AsyncMock(return_value={
        "id": "user123",
        "name": "Test User",
        "email": "test@example.com"
    })
    return client

@pytest.mark.asyncio
async def test_service_with_mock(mock_user_service_client):
    service = UserProfileService(user_client=mock_user_service_client)
    result = await service.get_user_profile("user123")

    # Verify the mock was called correctly
    mock_user_service_client.get_user_details.assert_called_once_with("user123")
    assert result["name"] == "Test User"
```

## 🔧 Development Workflow

### Daily Development Commands

```bash
# Start development server
make dev

# Run code quality checks
make lint          # Check code style
make typecheck     # Check types with pyrefly
make test          # Run tests
make check-all     # Run everything

# Documentation and development
make docs          # Open API docs in browser
make clean         # Remove cache files
make change-name   # Change service name throughout project
```

### Code Quality Tools

- **pyrefly** - Catches type errors before runtime with blazing speed
- **ruff** - Ensures consistent code style and formatting
- **pytest** - Comprehensive test coverage

### Pre-commit Hooks

```bash
# Install pre-commit hooks (runs checks automatically before commits)
make pre-commit-install

# Run hooks on all files manually
make pre-commit-run
```

## 🚢 Production Deployment

### Docker Deployment

This template includes a production-ready Docker setup with multi-stage builds, security best practices, and health checks.

#### Building and Running with Docker

```bash
# Build Docker image (uses your service name from pyproject.toml)
make docker-build

# Run container locally with environment variables
make docker-run

# Or build and run manually:
docker build -t my-microservice .
docker run -p 8000:8000 --env-file .env my-microservice
```

#### Docker Configuration Details

The included `Dockerfile` provides:

- **Multi-stage build** for smaller production images
- **Python 3.12-slim** base image for security and size optimization
- **UV package manager** for fast dependency installation
- **Non-root user** execution for enhanced security
- **Health check** endpoint for container orchestration
- **Proper caching** of dependencies for faster rebuilds

#### Environment Setup for Docker

**Required**: Create a `.env` file before running the container:

```bash
# Copy the example and customize for your environment
cp .env.example .env

# Edit with your configuration
nano .env
```

**Example production `.env` file:**

```env
# Application settings
APP_NAME="My Production Service"
APP_VERSION="1.0.0"
DEBUG=false

# Server settings (container internal)
HOST=0.0.0.0
PORT=8000

# External service URLs (update with your actual services)
EXTERNAL_SERVICE_A_URL=https://prod-api.service-a.com
EXTERNAL_SERVICE_B_URL=https://prod-api.service-b.com

# HTTP client settings
HTTP_TIMEOUT=10.0
HTTP_RETRIES=2

# Logging settings
LOG_LEVEL=INFO
```

#### Docker Commands Reference

```bash
# Development workflow
make docker-build          # Build image with current service name
make docker-run            # Run with .env file mounted

# Manual Docker commands
docker build -t my-service .                           # Build image
docker run -p 8000:8000 --env-file .env my-service    # Run with env file
docker run -d -p 8000:8000 --env-file .env my-service # Run in background

# Debugging container issues
docker logs <container-id>                     # View container logs
docker exec -it <container-id> /bin/bash      # Access running container
docker inspect <container-id>                 # Inspect container details
```

#### Health Checks and Monitoring

The Docker container includes built-in health checks:

```bash
# Check health endpoint
curl http://localhost:8000/health
# Returns: {"status": "healthy", "version": "1.0.0", "timestamp": "..."}

# Docker health check status
docker ps  # Shows health status in STATUS column

# Manual health check (same as Docker uses)
curl -f http://localhost:8000/health || echo "Health check failed"
```

The health check configuration in the Dockerfile:
- **Interval**: 30 seconds between checks
- **Timeout**: 30 seconds per check
- **Start period**: 5 seconds before first check
- **Retries**: 3 failed checks before marking unhealthy

#### Container Orchestration

For **Kubernetes**, **Docker Swarm**, or **AWS ECS**, the health check endpoint can be used for:
- **Liveness probes**: `/health` endpoint
- **Readiness probes**: `/health` endpoint
- **Load balancer health checks**: `/health` endpoint

Example Kubernetes deployment snippet:

```yaml
livenessProbe:
  httpGet:
    path: /health
    port: 8000
  initialDelaySeconds: 30
  periodSeconds: 30
readinessProbe:
  httpGet:
    path: /health
    port: 8000
  initialDelaySeconds: 5
  periodSeconds: 10
```

#### Troubleshooting Docker Issues

**Common problems and solutions:**

1. **Container fails to start:**
   ```bash
   # Check if .env file exists and has correct format
   docker run --env-file .env my-service
   # View detailed error logs
   docker logs <container-id>
   ```

2. **Permission issues:**
   ```bash
   # The container runs as non-root user 'appuser'
   # Ensure your .env file is readable
   chmod 644 .env
   ```

3. **Port already in use:**
   ```bash
   # Use different port mapping
   docker run -p 8001:8000 --env-file .env my-service
   ```

4. **Environment variables not loading:**
   ```bash
   # Verify .env file format (no spaces around =)
   # Check file contents
   cat .env
   # Test with inline environment variables
   docker run -e APP_NAME="Test Service" -p 8000:8000 my-service
   ```

## 🔧 Template Customization

### Renaming Your Service

The template comes with a powerful `make change-name` command that updates your service name throughout the entire project:

```bash
# Change from default "fastapi-base-service" to your service name
make change-name name=user-profile-service

# Or for a different service
make change-name name=payment-gateway-service
```

**What gets updated automatically:**
- `pyproject.toml` - Package name and metadata
- `.env.example` - APP_NAME with proper capitalization
- `.github/workflows/ci.yml` - Docker image names in CI/CD
- All Docker commands will use the new service name

**Example transformation:**
```bash
# Before
name = "fastapi-base-service"
APP_NAME="Fastapi Base Service"
docker build -t fastapi-base-service .

# After running: make change-name name=user-profile-service
name = "user-profile-service"
APP_NAME="User Profile Service"
docker build -t user-profile-service .
```

### Initial Setup Commands

If you're setting up the template for the first time, here are the essential commands that aren't covered in the basic quick start:

```bash
# 1. Install UV (if not already installed)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Install all dependencies (including dev tools)
make dev-install

# 3. Set up pre-commit hooks (recommended)
make pre-commit-install

# 4. Customize your service name
make change-name name=your-service-name

# 5. Update your environment variables
cp .env.example .env
# Then edit .env with your actual configuration

# 6. Run all quality checks to ensure everything works
make check-all
```

**Essential commands for development:**
```bash
# Daily development workflow
make dev           # Start development server
make docs          # Open API documentation in browser
make check-all     # Run linting, type checking, and tests
make test          # Run tests only
make lint          # Check code style
make typecheck     # Check types with pyrefly

# Docker workflow
make docker-build  # Build with your service name
make docker-run    # Run container locally
```

## 📋 Common Patterns and Examples

### Adding a New External Service

1. **Add client class** in `app/clients/external_client.py`
2. **Add URL to config** in `app/config.py` and `.env`
3. **Register in DI container** in `app/dependencies.py`
4. **Inject into service** in your business service
5. **Write tests** with mocked client

### Handling External Service Failures

The template shows how to handle failures gracefully:

```python
async def robust_external_call(self):
    try:
        result = await self.external_client.get_data()
        return result
    except httpx.HTTPError as e:
        logger.warning("External service failed", error=str(e))
        return {"error": "Service unavailable", "fallback": True}
```

### Adding Authentication

```python
# In your client class
class AuthenticatedClient(BaseClient):
    def __init__(self, http_client: httpx.AsyncClient, base_url: str, api_key: str):
        super().__init__(http_client, base_url)
        self.api_key = api_key

    async def _make_request(self, method: str, endpoint: str, **kwargs):
        headers = kwargs.setdefault("headers", {})
        headers["Authorization"] = f"Bearer {self.api_key}"
        return await super()._make_request(method, endpoint, **kwargs)
```

## 🆘 Troubleshooting

### Common Issues

1. **UV not found**: Install UV package manager first:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   # Then restart your terminal or run: source ~/.bashrc
   ```

2. **Import Errors**: Make sure you've run `make dev-install`
3. **Type Errors**: Run `make typecheck` to see pyrefly issues
4. **Test Failures**: Check that all external services are properly mocked
5. **Docker Issues**: Ensure `.env` file exists and has correct values
6. **Pre-commit hooks failing**: Run `make pre-commit-install` to set them up

### Getting Help

- Check the logs: structured logging provides detailed error information
- Use the debugger: set breakpoints in your IDE
- Run tests individually: `uv run pytest tests/unit/test_specific.py -v -s`

## 🎓 Next Steps

Once you have your microservice working:

1. **Add more endpoints** following the same pattern
2. **Add authentication and authorization** if needed
3. **Set up monitoring** and alerts
4. **Configure CI/CD** using the included GitHub Actions
5. **Deploy to your cloud provider** using the Docker container

## 📊 ELK Stack & OpenTelemetry Integration

This template includes comprehensive observability with the ELK (Elasticsearch, Logstash, Kibana) stack and OpenTelemetry for distributed tracing, structured logging, and metrics collection.

### 🏗️ Observability Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   FastAPI App   │───▶│ OpenTelemetry   │───▶│  Elasticsearch  │
│                 │    │   Collector     │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │              ┌─────────────────┐              │
         └─────────────▶│    Logstash     │──────────────┘
                        │                 │
                        └─────────────────┘
                                 │
                        ┌─────────────────┐
                        │     Kibana      │◀── Dashboard & Visualization
                        │                 │
                        └─────────────────┘
```

### 🚀 Observability Features

- **Distributed Tracing**: End-to-end request tracing with OpenTelemetry
- **Structured Logging**: JSON logs with trace correlation and request IDs
- **Metrics Collection**: Application performance and business metrics
- **Real-time Monitoring**: Live dashboards and visualization in Kibana
- **Log Aggregation**: Centralized logging with powerful search capabilities
- **Auto-Instrumentation**: Automatic tracing of HTTP requests, external APIs, and database calls

### 📋 Observability Stack

- **OpenTelemetry** - Distributed tracing and metrics collection
- **Elasticsearch** - Search and analytics engine for logs and traces
- **Logstash** - Log processing and enrichment pipeline
- **Kibana** - Visualization and dashboard platform
- **OpenTelemetry Collector** - Telemetry data processing and export

### 🔧 Quick Start with ELK Stack

#### Option 1: Docker Compose (Development)

1. **Start the complete ELK stack:**
   ```bash
   make elk-up
   ```

2. **Wait for all services to be ready** (2-3 minutes):
   ```bash
   # Check service status
   docker-compose -f docker-compose.elk.yml ps

   # View logs
   make elk-logs
   ```

3. **Access your observability platform:**
   - **FastAPI App**: http://localhost:8000
   - **API Documentation**: http://localhost:8000/docs
   - **Kibana Dashboard**: http://localhost:5601
   - **Elasticsearch API**: http://localhost:9200

#### Option 2: Kubernetes with Minikube (Production-like)

1. **Deploy to Minikube with full ELK stack:**
   ```bash
   make k8s-deploy
   ```

2. **Add local DNS entries** (as shown by setup script):
   ```bash
   # Add to /etc/hosts
   sudo echo "$(minikube ip)    fastapi-app.local" >> /etc/hosts
   sudo echo "$(minikube ip)    kibana.local" >> /etc/hosts
   ```

3. **Access services:**
   - **FastAPI App**: http://fastapi-app.local
   - **API Documentation**: http://fastapi-app.local/docs
   - **Kibana Dashboard**: http://kibana.local

### 📊 Understanding Your Observability Data

#### Request Tracing

Every request automatically gets:
- **Unique Request ID**: For correlation across all logs
- **Trace ID & Span ID**: For distributed tracing across services
- **Performance Metrics**: Request duration, status codes, error details

Example structured log entry:
```json
{
  "@timestamp": "2024-01-15T10:30:45.123Z",
  "level": "INFO",
  "message": "Request completed",
  "request_id": "550e8400-e29b-41d4-a716-446655440000",
  "trace_id": "4bf92f3577b34da6a3ce929d0e0e4736",
  "span_id": "00f067aa0ba902b7",
  "method": "POST",
  "path": "/process",
  "status_code": 200,
  "duration_ms": 45.67,
  "service": "fastapi-base-service",
  "version": "0.1.0",
  "client_ip": "192.168.1.100"
}
```

#### Automatic Instrumentation

The application automatically traces:
- **Incoming HTTP requests** with full request/response details
- **Outgoing HTTP calls** to external services (httpx, requests)
- **Business logic spans** with custom attributes
- **Error tracking** with stack traces and context

### 🔍 Using Kibana for Observability

#### Initial Setup

1. **Access Kibana**: http://localhost:5601 or http://kibana.local
2. **Create Index Patterns**:
   - Navigate to Stack Management → Index Patterns
   - Create pattern: `fastapi-logs-*` (for application logs)
   - Create pattern: `fastapi-traces-*` (for distributed traces)
   - Create pattern: `fastapi-metrics-*` (for application metrics)

#### Powerful Search Queries

**Find all errors in the last hour:**
```
level:ERROR AND @timestamp:[now-1h TO now]
```

**Trace a specific request end-to-end:**
```
request_id:"550e8400-e29b-41d4-a716-446655440000"
```

**Identify slow requests (>1000ms):**
```
duration_ms:>1000 AND @timestamp:[now-24h TO now]
```

**Monitor specific API endpoints:**
```
path:"/process" AND method:"POST" AND status_code:[400 TO 599]
```

#### Creating Operational Dashboards

Build comprehensive dashboards with:
1. **Request Rate Over Time** - Line chart showing RPS
2. **Response Time Percentiles** - P50, P95, P99 latency trends
3. **Error Rate Monitoring** - Percentage of failed requests
4. **Top API Endpoints** - Most frequently called endpoints
5. **Status Code Distribution** - 2xx/4xx/5xx breakdown
6. **Geographic Request Distribution** - If client IPs are logged

### 🛠️ Observability Configuration

#### Environment Variables for ELK Integration

```bash
# ELK Stack Configuration
ELASTICSEARCH_URL=http://localhost:9200
ELASTICSEARCH_INDEX=fastapi-logs

# OpenTelemetry Configuration
OTEL_SERVICE_NAME=fastapi-base-service
OTEL_SERVICE_VERSION=0.1.0
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
OTEL_RESOURCE_ATTRIBUTES=service.namespace=microservices,deployment.environment=development

# Observability Feature Toggles
ENABLE_TRACING=true
ENABLE_METRICS=true
ENABLE_LOGGING=true
```

#### Custom Instrumentation in Your Code

Add business-specific tracing to your services:

```python
from opentelemetry import trace
from app.observability import get_logger

tracer = trace.get_tracer(__name__)
logger = get_logger(__name__)

async def process_user_data(user_id: str, data: dict):
    with tracer.start_as_current_span("process_user_data") as span:
        # Add business context to spans
        span.set_attribute("user.id", user_id)
        span.set_attribute("data.size", len(str(data)))

        # Structured logging with context
        logger.info("Processing user data",
                   user_id=user_id,
                   data_type=type(data).__name__)

        try:
            # Your business logic here
            result = await your_business_logic(user_id, data)

            span.set_attribute("processing.status", "success")
            span.set_attribute("result.items_count", len(result))

            return result

        except Exception as e:
            span.record_exception(e)
            span.set_status(trace.Status(trace.StatusCode.ERROR, str(e)))
            logger.error("User data processing failed",
                        user_id=user_id, error=str(e))
            raise
```

### 📈 Production Monitoring

#### Key Metrics to Monitor

1. **Request Rate (RPS)**: Requests per second trending
2. **Error Rate**: Percentage of 4xx/5xx responses
3. **Response Time**: 95th percentile latency
4. **Throughput**: Successful requests per minute
5. **Service Health**: Health check endpoint status
6. **Resource Usage**: CPU, memory, and disk utilization

#### Setting Up Alerts

Create proactive alerts in Kibana for:
- **High Error Rate**: >5% errors in 5-minute window
- **Slow Response Times**: 95th percentile >1000ms
- **Request Rate Drops**: >50% decrease in traffic
- **Service Unavailability**: Health check failures

### 🧹 Observability Maintenance

#### Managing Data Retention

Configure Elasticsearch lifecycle management:

```bash
# Set up 30-day retention policy
curl -X PUT "localhost:9200/_ilm/policy/fastapi-logs-policy" \
  -H 'Content-Type: application/json' -d'
{
  "policy": {
    "phases": {
      "hot": {
        "actions": {
          "rollover": {
            "max_size": "5GB",
            "max_age": "1d"
          }
        }
      },
      "delete": {
        "min_age": "30d"
      }
    }
  }
}'
```

#### Observability Commands

```bash
# ELK Stack Management (Docker Compose)
make elk-up              # Start ELK stack
make elk-down            # Stop ELK stack
make elk-logs            # View all service logs

# Kubernetes ELK Deployment
make k8s-deploy          # Deploy full stack to Minikube
make k8s-status          # Check deployment status
make k8s-logs            # View application logs
make k8s-cleanup         # Remove all resources

# Health Checks
curl http://localhost:9200/_cluster/health  # Elasticsearch health
curl http://localhost:8000/health           # Application health
```

### 🐛 Troubleshooting Observability

#### Common Issues and Solutions

**Elasticsearch won't start:**
```bash
# Increase virtual memory
sudo sysctl -w vm.max_map_count=262144

# Check available resources
docker stats
```

**No logs appearing in Kibana:**
1. Verify index patterns exist and match your data
2. Check time range in Kibana (last 15 minutes → last 24 hours)
3. Verify application is sending logs to Elasticsearch:
   ```bash
   curl "localhost:9200/fastapi-logs-*/_search?pretty"
   ```

**OpenTelemetry traces not appearing:**
1. Check OpenTelemetry Collector logs:
   ```bash
   docker-compose -f docker-compose.elk.yml logs otel-collector
   ```
2. Verify OTLP endpoint configuration in application
3. Ensure traces index pattern is created in Kibana

### 🔒 Security Best Practices

For production deployments:

1. **Enable Elasticsearch Security**: Configure authentication and TLS
2. **Secure Kibana Access**: Implement proper authentication
3. **Network Isolation**: Use private networks and VPNs
4. **Data Encryption**: Enable TLS for all inter-service communication
5. **Log Sanitization**: Ensure no sensitive data appears in logs
6. **Access Control**: Implement role-based access to observability data

This comprehensive observability setup gives you enterprise-grade monitoring capabilities with minimal configuration. The ELK stack provides powerful insights into your application's behavior, performance, and health, making it easy to identify and resolve issues quickly.

This template gives you a solid foundation to build upon. Each component is designed to be easily extendable and thoroughly testable. Happy coding! 🚀
