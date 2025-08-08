.PHONY: help install dev-install test lint typecheck format run dev clean docker-build docker-run docs

# Default target
help:
	@echo "Available targets:"
	@echo "  install       - Install production dependencies"
	@echo "  dev-install   - Install development dependencies"
	@echo "  test          - Run tests"
	@echo "  lint          - Run flake8 linter"
	@echo "  typecheck     - Run pyrefly type checker"
	@echo "  format        - Format code (placeholder - add black if desired)"
	@echo "  run           - Run application in production mode"
	@echo "  dev           - Run application in development mode with auto-reload"
	@echo "  docs          - Open FastAPI automatic documentation in browser"
	@echo "  clean         - Clean up cache and temporary files"
	@echo "  docker-build  - Build Docker image"
	@echo "  docker-run    - Run Docker container"
	@echo "  change-name   - Change service name throughout project (usage: make change-name name=my-service)"
	@echo "  check-all     - Run all checks (lint, typecheck, test)"

# Dependency management
install:
	uv sync --no-dev

dev-install:
	uv sync --all-extras

# Testing
test:
	uv run pytest tests/ -v

test-cov:
	uv run pytest tests/ --cov=app --cov-report=html --cov-report=term

# Code quality
lint:
	uv run flake8 app tests

typecheck:
	uv run pyrefly check

format:
	@echo "Format target ready - add black or ruff if desired"
	@echo "Example: uv run black app tests"

# Running the application
run:
	uv run uvicorn app.main:app --host 0.0.0.0 --port 8000

dev:
	uv run uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

# Open API documentation
docs:
	@echo "Opening FastAPI documentation..."
	@echo "Make sure your service is running first with: make dev"
	@sleep 2
	@if command -v xdg-open >/dev/null 2>&1; then \
		xdg-open http://localhost:8000/docs; \
	elif command -v open >/dev/null 2>&1; then \
		open http://localhost:8000/docs; \
	elif command -v wslview >/dev/null 2>&1; then \
		wslview http://localhost:8000/docs; \
	else \
		echo "Please open http://localhost:8000/docs in your browser"; \
		echo "Alternative documentation available at: http://localhost:8000/redoc"; \
	fi

# Development workflow
check-all: lint typecheck test

# Cleanup
clean:
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	find . -type d -name "*.egg-info" -exec rm -rf {} +
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf dist/
	rm -rf build/

# Get service name from pyproject.toml
SERVICE_NAME := $(shell grep '^name = ' pyproject.toml | cut -d'"' -f2)

# Docker
docker-build:
	docker build -t $(SERVICE_NAME) .

docker-run:
	docker run -p 8000:8000 --env-file .env $(SERVICE_NAME)

# Change service name throughout the project
change-name:
	@if [ -z "$(name)" ]; then \
		echo "Usage: make change-name name=your-service-name"; \
		echo "Example: make change-name name=user-profile-service"; \
		exit 1; \
	fi
	@echo "Changing service name to: $(name)"
	@sed -i 's/^name = ".*"/name = "$(name)"/' pyproject.toml
	@sed -i 's/fastapi-base-service/$(name)/g' .github/workflows/ci.yml
	@sed -i 's/APP_NAME=".*"/APP_NAME="$(shell echo $(name) | sed 's/-/ /g' | sed 's/\b\w/\u&/g')"/' .env.example
	@echo "Service name changed successfully!"
	@echo "Remember to update your .env file with the new APP_NAME"

# Pre-commit setup (if using pre-commit)
pre-commit-install:
	uv run pre-commit install

pre-commit-run:
	uv run pre-commit run --all-files
