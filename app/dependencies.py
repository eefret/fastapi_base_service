from dependency_injector import containers, providers
import httpx

from app.config import settings
from app.clients.external_client import ExternalServiceAClient, ExternalServiceBClient
from app.services.business_service import BusinessService


class Container(containers.DeclarativeContainer):
    # Configuration
    config = providers.Object(settings)

    # HTTP client
    http_client = providers.Singleton(
        httpx.AsyncClient,
        timeout=settings.http_timeout,
        follow_redirects=True,
    )

    # External service clients
    external_service_a_client = providers.Factory(
        ExternalServiceAClient,
        http_client=http_client,
        base_url=settings.external_service_a_url,
    )

    external_service_b_client = providers.Factory(
        ExternalServiceBClient,
        http_client=http_client,
        base_url=settings.external_service_b_url,
    )

    # Business services
    business_service = providers.Factory(
        BusinessService,
        service_a_client=external_service_a_client,
        service_b_client=external_service_b_client,
    )


# Create global container instance
container = Container()


# Dependency functions for FastAPI
def get_business_service() -> BusinessService:
    return container.business_service()


def get_external_service_a_client() -> ExternalServiceAClient:
    return container.external_service_a_client()


def get_external_service_b_client() -> ExternalServiceBClient:
    return container.external_service_b_client()
