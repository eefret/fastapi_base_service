# Plantilla de Microservicio FastAPI

Una plantilla integral de microservicio FastAPI lista para producción, diseñada para desarrolladores que necesitan construir microservicios robustos y testeables con integraciones de APIs externas.

## 🎯 Lo que Proporciona Esta Plantilla

Esta plantilla te da todo lo necesario para construir un microservicio que:
- Recibe solicitudes HTTP
- Llama a múltiples APIs externas
- Procesa y combina datos
- Devuelve respuestas estructuradas
- Es completamente testeable con dependencias simuladas
- Está listo para despliegue en producción

## 🛠️ Stack Tecnológico y Por Qué Elegimos Cada Librería

### Framework Principal
- **FastAPI** - Framework web moderno y rápido de Python elegido por:
  - Documentación automática de API (OpenAPI/Swagger)
  - Validación de datos incorporada con Pydantic
  - Soporte nativo de async/await
  - Excelente integración con type hints
  - Alto rendimiento (comparable a NodeJS y Go)

### Herramientas de Desarrollo
- **UV** - Gestor de paquetes Python ultra-rápido elegido por:
  - 10-100x más rápido que pip para resolución de dependencias
  - Gestión de entornos virtuales incorporada
  - Mejor bloqueo de dependencias y builds reproducibles
  - Reemplazo moderno para pip-tools y virtualenv

- **pyrefly** - Verificador de tipos Python ultra-rápido elegido sobre PyRight/mypy porque:
  - Escrito en Rust para máximo rendimiento (10x+ más rápido que PyRight)
  - Verificación de tipos incremental extremadamente rápida
  - Arquitectura moderna diseñada para velocidad
  - Compatible con type hints de Python existentes
  - Mejor experiencia del desarrollador con loops de retroalimentación más rápidos

### Servidor Web y HTTP
- **uvicorn** - Servidor ASGI ultrarrápido elegido por:
  - Excelente rendimiento con código Python asíncrono
  - Soporte incorporado para funcionalidades de FastAPI
  - Auto-recarga durante el desarrollo
  - Listo para producción con gestión apropiada de procesos

- **httpx** - Cliente HTTP moderno elegido sobre requests porque:
  - Soporte nativo de async/await (crucial para rendimiento)
  - Soporte HTTP/2
  - Respuestas de streaming
  - Misma API que requests pero async-first

### Arquitectura y Patrones de Diseño
- **dependency-injector** - Framework DI profesional elegido por:
  - Separación clara de responsabilidades
  - Fácil testing con inyección de mocks
  - Gestión de configuración
  - Carga perezosa de dependencias
  - Mejor que gestión manual de dependencias

- **pydantic** - Librería de validación de datos elegida por:
  - Verificación y validación de tipos en tiempo de ejecución
  - Serialización/deserialización automática
  - Mensajes de error claros para datos inválidos
  - Integración perfecta con FastAPI
  - Gestión de configuraciones con variables de entorno

### Testing y Calidad
- **pytest** - Framework de testing estándar de Python elegido por:
  - Sintaxis de test simple y legible
  - Sistema de fixtures poderoso
  - Excelente ecosistema de plugins
  - Soporte de test asíncrono
  - Mejor que unittest para Python moderno

- **pytest-mock** - Utilidades de mocking elegidas porque:
  - Sintaxis más limpia que unittest.mock puro
  - Limpieza automática de mocks
  - Mejor integración con fixtures de pytest
  - Soporte AsyncMock para funciones async

- **ruff** - Linter y formateador Python ultra-rápido elegido por:
  - Escrito en Rust para máximo rendimiento (10-100x más rápido que flake8)
  - Herramienta todo-en-uno que combina linting y formateo
  - Compatible con herramientas y reglas Python existentes
  - Reemplazo moderno para flake8, black y otras herramientas

### Logging y Observabilidad
- **structlog** - Logging estructurado elegido sobre logging estándar porque:
  - Salida JSON para mejor parseo de logs
  - Variables de contexto para trazabilidad de requests
  - Mejor rendimiento que logging estándar
  - Logs más legibles durante desarrollo
  - Esencial para observabilidad de microservicios

### Contenedorización
- **Docker** - Contenedorización estándar de la industria elegida por:
  - Entornos consistentes entre dev/staging/prod
  - Fácil despliegue a cualquier proveedor de nube
  - Aislamiento y seguridad
  - Escalabilidad con orquestadores de contenedores

## 🚀 Guía de Inicio Rápido

### Prerrequisitos

- Python 3.12 o superior
- [Gestor de paquetes UV](https://github.com/astral-sh/uv) instalado
- Docker (opcional, para contenedorización)

### 1. Clonar y Configurar

```bash
# Clonar el repositorio
git clone <url-de-tu-repo>
cd fastapi_base_service

# Instalar gestor de paquetes UV (si no está instalado)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Instalar todas las dependencias (incluyendo herramientas de desarrollo)
make dev-install

# Copiar el archivo de entorno de ejemplo
cp .env.example .env

# (Opcional) Configurar hooks de pre-commit para calidad de código
make pre-commit-install
```

### 2. Configurar Tu Servicio

Edita el archivo `.env` con los detalles de tu servicio:

```env
# Información de tu servicio
APP_NAME="Mi Microservicio Increíble"
APP_VERSION="1.0.0"
DEBUG=true

# Configuración del servidor
HOST=0.0.0.0
PORT=8000

# APIs externas que llamará tu servicio
EXTERNAL_SERVICE_A_URL=https://api.servicio-a.ejemplo.com
EXTERNAL_SERVICE_B_URL=https://api.servicio-b.ejemplo.com

# Configuración del cliente HTTP
HTTP_TIMEOUT=30.0
HTTP_RETRIES=3

# Logging
LOG_LEVEL=INFO
```

### 3. Personalizar Nombre del Servicio (Opcional)

```bash
# Cambiar el nombre del servicio desde el default "fastapi-base-service"
make change-name name=mi-servicio-increible

# Esto actualiza:
# - Nombre del paquete en pyproject.toml
# - APP_NAME en .env.example
# - Workflow de GitHub Actions
# - Nombre de imagen Docker
```

### 4. Ejecutar Tu Servicio

```bash
# Iniciar en modo desarrollo (auto-recarga con cambios de código)
make dev

# Tu servicio ahora está ejecutándose en http://localhost:8000
# Abrir documentación API en navegador (en otra terminal)
make docs
```

### 5. Probar Que Todo Funciona

```bash
# Verificar endpoint de salud
curl http://localhost:8000/health

# Probar el endpoint principal
curl -X POST "http://localhost:8000/process" \
     -H "Content-Type: application/json" \
     -d '{"input_data": "hola mundo", "options": {"test": "true"}}'
```

## 📚 Documentación API

FastAPI genera automáticamente documentación API interactiva que puedes acceder mientras tu servicio está ejecutándose:

### Documentación Incorporada
```bash
# Iniciar tu servicio
make dev

# Abrir documentación API interactiva (en otra terminal)
make docs
```

**Endpoints de documentación disponibles:**
- **Swagger UI**: `http://localhost:8000/docs` (interactivo, probar APIs directamente)
- **ReDoc**: `http://localhost:8000/redoc` (documentación limpia e imprimible)
- **OpenAPI JSON**: `http://localhost:8000/openapi.json` (especificación API legible por máquina)

### Endpoints API por Defecto

- `GET /health` - Endpoint de verificación de salud
- `POST /process` - Endpoint principal de procesamiento de datos

**Pruébalo interactivamente:**
1. Ejecuta `make dev` para iniciar tu servicio
2. Ejecuta `make docs` para abrir la documentación interactiva
3. ¡Haz clic en cualquier endpoint para ver detalles y probarlo directamente en el navegador!

## 📁 Estructura del Proyecto Explicada

```
fastapi_base_service/
├── app/                          # Código principal de la aplicación
│   ├── main.py                   # Configuración FastAPI y rutas
│   ├── config.py                 # Gestión de configuración
│   ├── dependencies.py           # Configuración inyección de dependencias
│   ├── observability.py          # Configuración OpenTelemetry y logging
│   ├── clients/                  # Clientes de servicios externos
│   │   └── external_client.py    # Clases de cliente HTTP
│   ├── services/                 # Lógica de negocio
│   │   └── business_service.py   # Lógica de negocio principal
│   ├── models/                   # Modelos de datos
│   │   └── requests.py           # Modelos request/response
│   └── middleware/               # Middleware personalizado
│       ├── error_handler.py      # Manejo de errores
│       └── request_tracing.py    # Trazado y correlación de requests
├── tests/                        # Todos los tests
│   ├── conftest.py              # Configuración de test y fixtures
│   ├── unit/                    # Tests unitarios
│   └── integration/             # Tests de integración API
├── k8s/                         # Archivos de despliegue Kubernetes
│   ├── configs/                 # Archivos de configuración para servicios
│   │   ├── logstash/           # Pipeline y configuración Logstash
│   │   │   ├── config/
│   │   │   └── pipeline/
│   │   └── otel-collector/     # Configuración OpenTelemetry Collector
│   │       └── config.yml
│   ├── elasticsearch.yml       # Despliegue Elasticsearch
│   ├── fastapi-app.yml         # Despliegue aplicación FastAPI
│   ├── kibana.yml              # Despliegue Kibana
│   ├── otel-collector.yml      # Despliegue OpenTelemetry Collector
│   ├── namespace.yml           # Namespace Kubernetes
│   ├── setup-minikube.sh       # Configuración automatizada Minikube
│   └── README.md               # Instrucciones de despliegue
├── docker-compose.elk.yml       # Stack ELK para desarrollo
├── docker-compose.simple.yml    # Configuración simple FastAPI
├── .env.example                 # Plantilla variables de entorno
├── pyproject.toml              # Dependencias y configuración de herramientas
├── Makefile                    # Comandos de desarrollo
└── Dockerfile                  # Configuración de contenedor
```

## 🏛️ Inmersión Profunda en Arquitectura

### Patrón de Arquitectura General

Esta plantilla implementa un patrón de **Arquitectura Limpia** con **Inyección de Dependencias**, diseñado específicamente para microservicios que se integran con APIs externas. Así es como funcionan las capas:

```
┌─────────────────────────────────────────────────────────────┐
│                    Capa HTTP (FastAPI)                     │
│  ┌─────────────────┐  ┌──────────────────┐  ┌─────────────┐ │
│  │   Middleware    │  │   Rutas API      │  │ Validación  │ │
│  │ (Error, CORS,   │  │  (main.py)       │  │ (Pydantic)  │ │
│  │  Logging)       │  │                  │  │             │ │
│  └─────────────────┘  └──────────────────┘  └─────────────┘ │
└─────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                   Capa de Lógica de Negocio                │
│  ┌───────────────────────────────────────────────────────┐  │
│  │              Servicios de Negocio                     │  │
│  │         (services/business_service.py)                │  │
│  │  • Orquesta múltiples llamadas externas               │  │
│  │  • Implementa lógica de negocio                       │  │
│  │  • Maneja fallos graciosamente                        │  │
│  └───────────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                   Capa de Integración Externa              │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────┐  │
│  │  Cliente        │  │  Cliente        │  │  Cliente N  │  │
│  │  Servicio A     │  │  Servicio B     │  │             │  │
│  │ (Llamadas HTTP) │  │ (Llamadas HTTP) │  │(Llamadas HTTP)│  │
│  └─────────────────┘  └─────────────────┘  └─────────────┘  │
└─────────────────────────────────────────────────────────────┘
                                │
                                ▼
┌─────────────────────────────────────────────────────────────┐
│                     APIs Externas                          │
│   🌐 Servicio Externo A    🌐 Servicio Externo B          │
└─────────────────────────────────────────────────────────────┘
```

### Decisiones Arquitectónicas Clave

#### 1. **Contenedor de Inyección de Dependencias**
- **Por qué**: Facilita el testing permitiendo inyección de mocks
- **Cómo**: `dependency-injector` gestiona todas las dependencias
- **Beneficios**:
  - Fácil de testear (inyectar mocks)
  - Acoplamiento débil entre componentes
  - Configuración centralizada
  - Carga perezosa de recursos costosos

#### 2. **Diseño Async-First**
- **Por qué**: Los microservicios a menudo esperan por APIs externas
- **Cómo**: Todas las operaciones I/O usan async/await
- **Beneficios**:
  - Alta concurrencia con bajo uso de memoria
  - Puede manejar muchas solicitudes simultáneamente
  - Perfecto para cargas de trabajo I/O-bound (mayoría de microservicios)

#### 3. **Capa de Abstracción de Cliente**
- **Por qué**: Aísla la complejidad de APIs externas
- **Cómo**: Clase base de cliente con funcionalidad HTTP común
- **Beneficios**:
  - Manejo consistente de errores
  - Fácil de mockear para testing
  - Logging centralizado y lógica de reintentos
  - Puede intercambiar implementaciones fácilmente

#### 4. **Logging Estructurado con Trazabilidad de Requests**
- **Por qué**: Esencial para depurar sistemas distribuidos
- **Cómo**: Cada request obtiene ID único, logs JSON estructurados
- **Beneficios**:
  - Fácil rastrear requests a través de servicios
  - Logs buscables en producción
  - Preservación de contexto a través de llamadas async

### Ejemplo de Flujo de Datos

Esto es lo que sucede cuando llega una solicitud:

```python
# 1. Request llega al endpoint de FastAPI
@app.post("/process")
async def process_data(request: ProcessDataRequest, service = Depends(get_business_service)):

    # 2. Request es validado por Pydantic
    # 3. Inyección de dependencias proporciona servicio de negocio
    # 4. Servicio de negocio orquesta llamadas externas

    result = await business_service.process_data(request.input_data, request.options)
    return ProcessDataResponse(**result)

# Dentro de BusinessService.process_data():
async def process_data(self, input_data: str, options: dict):
    # 5. Múltiples servicios externos llamados concurrentemente
    service_a_data, service_b_data = await asyncio.gather(
        self.service_a_client.get_data(input_data),      # Llamada concurrente 1
        self.service_b_client.fetch_metadata(input_data)  # Llamada concurrente 2
    )

    # 6. Lógica de negocio combina resultados
    processed_result = self._combine_data(input_data, service_a_data, service_b_data)

    # 7. Respuesta estructurada devuelta
    return {
        "processed_data": processed_result,
        "source_a_data": str(service_a_data),
        "source_b_data": str(service_b_data),
        "processing_time_ms": processing_time
    }
```

### Por Qué Esta Arquitectura Funciona para Microservicios

1. **Testeabilidad**: Cada dependencia es inyectada y mockeable
2. **Escalabilidad**: Diseño async maneja alta concurrencia
3. **Mantenibilidad**: Separación clara de responsabilidades
4. **Observabilidad**: Logging estructurado y manejo de errores
5. **Resistencia**: Manejo gracioso de fallos de servicios externos
6. **Experiencia del Desarrollador**: Seguridad de tipos y autocompletado en todas partes

### Arquitectura de Testing

La estrategia de testing refleja la arquitectura de la aplicación:

```
Tests Unitarios (tests/unit/)
├── test_business_service.py     # Testea lógica de negocio con clientes mockeados
├── test_clients.py              # Testea clientes HTTP con httpx mockeado
└── test_*.py                    # Otros tests unitarios

Tests de Integración (tests/integration/)
├── test_api.py                  # Testea endpoints FastAPI con servicios mockeados
└── test_*.py                    # Otros tests de integración

Configuración de Test (tests/conftest.py)
├── Fixtures mock para todas las dependencias externas
├── Configuración de cliente de test
└── Utilidades de test compartidas
```

Esta arquitectura asegura que:
- **Tests unitarios** son rápidos (sin llamadas externas)
- **Tests de integración** verifican el contrato API
- **Todas las dependencias externas son mockeables**
- **Tests están aislados y son predecibles**

## 🏗️ Cómo Construir Tu Propio Microservicio

Sigue esta guía paso a paso para transformar esta plantilla en tu propio microservicio.

### Paso 1: Definir Tus Modelos de Datos

Comienza definiendo qué datos recibirá y devolverá tu servicio.

**Ejemplo: Construyendo un Servicio de Perfil de Usuario**

Edita `app/models/requests.py`:

```python
from pydantic import BaseModel, Field
from typing import Optional

class UserProfileRequest(BaseModel):
    user_id: str = Field(description="ID de usuario para obtener perfil")
    include_preferences: bool = Field(default=True, description="Incluir preferencias de usuario")
    include_history: bool = Field(default=False, description="Incluir historial de usuario")

class UserProfileResponse(BaseModel):
    user_id: str = Field(description="ID de usuario")
    name: str = Field(description="Nombre completo del usuario")
    email: str = Field(description="Email del usuario")
    preferences: Optional[dict] = Field(default=None, description="Preferencias de usuario")
    history: Optional[list] = Field(default=None, description="Historial de usuario")
    last_updated: str = Field(description="Timestamp de última actualización")
```

### Paso 2: Crear Clientes de Servicios Externos

Define las APIs externas que llamará tu servicio.

**Ejemplo: Clientes de Servicio de Usuario y Servicio de Analytics**

Edita `app/clients/external_client.py` y agrega tus clientes:

```python
class UserServiceClient(BaseClient):
    """Cliente para el Servicio de Gestión de Usuarios"""

    async def get_user_details(self, user_id: str) -> dict:
        """Obtener información básica del usuario"""
        return await self._make_request(
            "GET",
            f"/api/v1/users/{user_id}"
        )

    async def get_user_preferences(self, user_id: str) -> dict:
        """Obtener preferencias del usuario"""
        return await self._make_request(
            "GET",
            f"/api/v1/users/{user_id}/preferences"
        )

class AnalyticsServiceClient(BaseClient):
    """Cliente para el Servicio de Analytics"""

    async def get_user_history(self, user_id: str, limit: int = 10) -> dict:
        """Obtener historial de actividad del usuario"""
        return await self._make_request(
            "GET",
            f"/api/v1/analytics/users/{user_id}/history",
            params={"limit": limit}
        )
```

### Paso 3: Actualizar Configuración

Agrega las URLs de tus nuevos servicios externos a `app/config.py`:

```python
class Settings(BaseSettings):
    # ... configuraciones existentes ...

    # URLs de tus servicios externos
    user_service_url: str = Field(default="", description="URL base del Servicio de Usuario")
    analytics_service_url: str = Field(default="", description="URL base del Servicio de Analytics")
```

Y actualiza tu archivo `.env`:

```env
USER_SERVICE_URL=https://api.usuarioservicio.com
ANALYTICS_SERVICE_URL=https://api.analytics.com
```

### Paso 4: Actualizar Inyección de Dependencias

Registra tus nuevos clientes en `app/dependencies.py`:

```python
from app.clients.external_client import UserServiceClient, AnalyticsServiceClient
from app.services.user_profile_service import UserProfileService

class Container(containers.DeclarativeContainer):
    # ... proveedores existentes ...

    # Tus nuevos clientes de servicio
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

    # Tu servicio de negocio
    user_profile_service = providers.Factory(
        UserProfileService,
        user_client=user_service_client,
        analytics_client=analytics_service_client,
    )

# Funciones de dependencia para FastAPI
def get_user_profile_service() -> UserProfileService:
    return container.user_profile_service()
```

### Paso 5: Implementar Lógica de Negocio

Crea tu servicio de negocio. Reemplaza `app/services/business_service.py` o crea un archivo nuevo:

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
        """Obtener perfil completo de usuario de múltiples servicios"""

        logger.info("Obteniendo perfil de usuario", user_id=user_id)

        # Siempre obtener detalles básicos del usuario
        tasks = [self.user_client.get_user_details(user_id)]

        # Condicionalmente obtener datos adicionales
        if include_preferences:
            tasks.append(self.user_client.get_user_preferences(user_id))

        if include_history:
            tasks.append(self.analytics_client.get_user_history(user_id))

        # Ejecutar todas las solicitudes concurrentemente
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Procesar resultados
        user_details = results[0] if not isinstance(results[0], Exception) else {}

        preferences = None
        if include_preferences and len(results) > 1:
            preferences = results[1] if not isinstance(results[1], Exception) else None

        history = None
        if include_history:
            history_index = 2 if include_preferences else 1
            if len(results) > history_index:
                history = results[history_index] if not isinstance(results[history_index], Exception) else None

        # Combinar todos los datos
        return {
            "user_id": user_id,
            "name": user_details.get("name", "Desconocido"),
            "email": user_details.get("email", ""),
            "preferences": preferences,
            "history": history,
            "last_updated": datetime.utcnow().isoformat(),
        }
```

### Paso 6: Crear Endpoints API

Actualiza `app/main.py` para agregar tus nuevos endpoints:

```python
from app.models.requests import UserProfileRequest, UserProfileResponse
from app.services.user_profile_service import UserProfileService
from app.dependencies import get_user_profile_service

# Agregar esto a tu app FastAPI
@app.post("/user-profile", response_model=UserProfileResponse)
async def get_user_profile(
    request: UserProfileRequest,
    profile_service: UserProfileService = Depends(get_user_profile_service),
) -> UserProfileResponse:
    """Obtener perfil completo de usuario"""
    try:
        result = await profile_service.get_user_profile(
            user_id=request.user_id,
            include_preferences=request.include_preferences,
            include_history=request.include_history,
        )

        return UserProfileResponse(**result)

    except Exception as e:
        logger.error("Error al obtener perfil de usuario", error=str(e), user_id=request.user_id)
        raise HTTPException(status_code=500, detail="Error al obtener perfil")
```

### Paso 7: Escribir Tests

Crea tests para tu nuevo servicio. La plantilla proporciona ejemplos comprehensivos.

**Ejemplo: Testear tu Servicio de Perfil de Usuario**

```python
# tests/unit/test_user_profile_service.py
import pytest
from unittest.mock import AsyncMock

from app.services.user_profile_service import UserProfileService

@pytest.mark.asyncio
async def test_get_user_profile_success():
    """Test de obtención exitosa de perfil de usuario"""
    # Organizar
    mock_user_client = AsyncMock()
    mock_analytics_client = AsyncMock()

    mock_user_client.get_user_details.return_value = {
        "name": "Juan Pérez",
        "email": "juan@ejemplo.com"
    }
    mock_user_client.get_user_preferences.return_value = {
        "theme": "oscuro",
        "notifications": True
    }

    service = UserProfileService(
        user_client=mock_user_client,
        analytics_client=mock_analytics_client
    )

    # Actuar
    result = await service.get_user_profile("user123")

    # Verificar
    assert result["user_id"] == "user123"
    assert result["name"] == "Juan Pérez"
    assert result["email"] == "juan@ejemplo.com"
    assert result["preferences"]["theme"] == "oscuro"

    # Verificar que se hicieron las llamadas externas
    mock_user_client.get_user_details.assert_called_once_with("user123")
    mock_user_client.get_user_preferences.assert_called_once_with("user123")
```

## 🧪 Testear Tu Microservicio

### Entendiendo la Estrategia de Mocking

La plantilla usa **pytest-mock** y **unittest.mock** para mocking:

- **`AsyncMock`** - Para mockear funciones async y clientes HTTP
- **`MagicMock`** - Para mockear funciones síncronas
- **`pytest-mock`** - Proporciona fixtures y utilidades convenientes

### Ejecutar Tests

```bash
# Ejecutar todos los tests
make test

# Ejecutar con reporte de cobertura
make test-cov

# Ejecutar archivo de test específico
uv run pytest tests/unit/test_user_profile_service.py -v

# Ejecutar tests con salida detallada
uv run pytest tests/ -v -s
```

### Estructura de Tests

La plantilla proporciona tres tipos de tests:

1. **Tests Unitarios** (`tests/unit/`) - Testear componentes individuales con dependencias mockeadas
2. **Tests de Integración** (`tests/integration/`) - Testear endpoints API con servicios mockeados
3. **Fixtures de Test** (`tests/conftest.py`) - Objetos mock reutilizables y configuración

### Ejemplo: Mockear Servicios Externos

```python
@pytest.fixture
async def mock_user_service_client():
    """Mock para cliente de servicio de usuario"""
    client = AsyncMock()
    client.get_user_details = AsyncMock(return_value={
        "id": "user123",
        "name": "Usuario Test",
        "email": "test@ejemplo.com"
    })
    return client

@pytest.mark.asyncio
async def test_service_with_mock(mock_user_service_client):
    service = UserProfileService(user_client=mock_user_service_client)
    result = await service.get_user_profile("user123")

    # Verificar que el mock fue llamado correctamente
    mock_user_service_client.get_user_details.assert_called_once_with("user123")
    assert result["name"] == "Usuario Test"
```

## 🔧 Flujo de Desarrollo

### Comandos de Desarrollo Diarios

```bash
# Iniciar servidor de desarrollo
make dev

# Ejecutar verificaciones de calidad de código
make lint          # Verificar estilo de código
make typecheck     # Verificar tipos con pyrefly
make test          # Ejecutar tests
make check-all     # Ejecutar todo

# Documentación y desarrollo
make docs          # Abrir documentación API en navegador
make clean         # Eliminar archivos de caché
make change-name   # Cambiar nombre de servicio en todo el proyecto
```

### Herramientas de Calidad de Código

- **pyrefly** - Detecta errores de tipo antes del tiempo de ejecución con velocidad ultrarrápida
- **ruff** - Asegura estilo de código consistente y formateo
- **pytest** - Cobertura de test comprehensiva

### Hooks de Pre-commit

```bash
# Instalar hooks de pre-commit (ejecuta verificaciones automáticamente antes de commits)
make pre-commit-install

# Ejecutar hooks en todos los archivos manualmente
make pre-commit-run
```

## 🚢 Despliegue en Producción

### Despliegue Docker

Esta plantilla incluye una configuración Docker lista para producción con builds multi-etapa, mejores prácticas de seguridad y health checks.

#### Construir y Ejecutar con Docker

```bash
# Construir imagen Docker (usa tu nombre de servicio de pyproject.toml)
make docker-build

# Ejecutar contenedor localmente con variables de entorno
make docker-run

# O construir y ejecutar manualmente:
docker build -t mi-microservicio .
docker run -p 8000:8000 --env-file .env mi-microservicio
```

#### Detalles de Configuración Docker

El `Dockerfile` incluido proporciona:

- **Build multi-etapa** para imágenes de producción más pequeñas
- **Imagen base Python 3.12-slim** para optimización de seguridad y tamaño
- **Gestor de paquetes UV** para instalación rápida de dependencias
- **Ejecución de usuario no-root** para seguridad mejorada
- **Endpoint de health check** para orquestación de contenedores
- **Caché apropiado** de dependencias para rebuilds más rápidos

#### Configuración de Entorno para Docker

**Requerido**: Crear un archivo `.env` antes de ejecutar el contenedor:

```bash
# Copiar el ejemplo y personalizar para tu entorno
cp .env.example .env

# Editar con tu configuración
nano .env
```

**Ejemplo de archivo `.env` para producción:**

```env
# Configuración de aplicación
APP_NAME="Mi Servicio de Producción"
APP_VERSION="1.0.0"
DEBUG=false

# Configuración de servidor (interno del contenedor)
HOST=0.0.0.0
PORT=8000

# URLs de servicios externos (actualizar con tus servicios reales)
EXTERNAL_SERVICE_A_URL=https://prod-api.servicio-a.com
EXTERNAL_SERVICE_B_URL=https://prod-api.servicio-b.com

# Configuración de cliente HTTP
HTTP_TIMEOUT=10.0
HTTP_RETRIES=2

# Configuración de logging
LOG_LEVEL=INFO
```

#### Referencia de Comandos Docker

```bash
# Flujo de desarrollo
make docker-build          # Construir imagen con nombre de servicio actual
make docker-run            # Ejecutar con archivo .env montado

# Comandos Docker manuales
docker build -t mi-servicio .                           # Construir imagen
docker run -p 8000:8000 --env-file .env mi-servicio    # Ejecutar con archivo env
docker run -d -p 8000:8000 --env-file .env mi-servicio # Ejecutar en segundo plano

# Depurar problemas de contenedor
docker logs <container-id>                     # Ver logs del contenedor
docker exec -it <container-id> /bin/bash      # Acceder a contenedor en ejecución
docker inspect <container-id>                 # Inspeccionar detalles del contenedor
```

#### Health Checks y Monitoreo

El contenedor Docker incluye health checks incorporados:

```bash
# Verificar endpoint de salud
curl http://localhost:8000/health
# Retorna: {"status": "healthy", "version": "1.0.0", "timestamp": "..."}

# Estado de health check de Docker
docker ps  # Muestra estado de salud en columna STATUS

# Health check manual (igual que usa Docker)
curl -f http://localhost:8000/health || echo "Health check falló"
```

La configuración de health check en el Dockerfile:
- **Intervalo**: 30 segundos entre verificaciones
- **Timeout**: 30 segundos por verificación
- **Período de inicio**: 5 segundos antes de primera verificación
- **Reintentos**: 3 verificaciones fallidas antes de marcar como no saludable

#### Orquestación de Contenedores

Para **Kubernetes**, **Docker Swarm**, o **AWS ECS**, el endpoint de health check puede usarse para:
- **Sondas de vida**: endpoint `/health`
- **Sondas de preparación**: endpoint `/health`
- **Health checks de load balancer**: endpoint `/health`

Ejemplo de snippet de despliegue Kubernetes:

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

#### Solución de Problemas Docker

**Problemas comunes y soluciones:**

1. **El contenedor falla al iniciar:**
   ```bash
   # Verificar si existe archivo .env y tiene formato correcto
   docker run --env-file .env mi-servicio
   # Ver logs de error detallados
   docker logs <container-id>
   ```

2. **Problemas de permisos:**
   ```bash
   # El contenedor ejecuta como usuario no-root 'appuser'
   # Asegurar que tu archivo .env sea legible
   chmod 644 .env
   ```

3. **Puerto ya en uso:**
   ```bash
   # Usar mapeo de puerto diferente
   docker run -p 8001:8000 --env-file .env mi-servicio
   ```

4. **Variables de entorno no cargan:**
   ```bash
   # Verificar formato de archivo .env (sin espacios alrededor de =)
   # Verificar contenido del archivo
   cat .env
   # Probar con variables de entorno inline
   docker run -e APP_NAME="Servicio Test" -p 8000:8000 mi-servicio
   ```

## 🔧 Personalización de Plantilla

### Renombrar Tu Servicio

La plantilla viene con un comando poderoso `make change-name` que actualiza el nombre de tu servicio en todo el proyecto:

```bash
# Cambiar desde el default "fastapi-base-service" a tu nombre de servicio
make change-name name=servicio-perfil-usuario

# O para un servicio diferente
make change-name name=servicio-gateway-pago
```

**Lo que se actualiza automáticamente:**
- `pyproject.toml` - Nombre de paquete y metadata
- `.env.example` - APP_NAME con capitalización apropiada
- `.github/workflows/ci.yml` - Nombres de imagen Docker en CI/CD
- Todos los comandos Docker usarán el nuevo nombre de servicio

**Ejemplo de transformación:**
```bash
# Antes
name = "fastapi-base-service"
APP_NAME="Fastapi Base Service"
docker build -t fastapi-base-service .

# Después de ejecutar: make change-name name=servicio-perfil-usuario
name = "servicio-perfil-usuario"
APP_NAME="Servicio Perfil Usuario"
docker build -t servicio-perfil-usuario .
```

### Comandos de Configuración Inicial

Si estás configurando la plantilla por primera vez, aquí están los comandos esenciales que no se cubren en el inicio rápido básico:

```bash
# 1. Instalar UV (si no está instalado)
curl -LsSf https://astral.sh/uv/install.sh | sh

# 2. Instalar todas las dependencias (incluyendo herramientas dev)
make dev-install

# 3. Configurar hooks de pre-commit (recomendado)
make pre-commit-install

# 4. Personalizar nombre de tu servicio
make change-name name=tu-nombre-servicio

# 5. Actualizar tus variables de entorno
cp .env.example .env
# Luego editar .env con tu configuración actual

# 6. Ejecutar todas las verificaciones de calidad para asegurar que todo funciona
make check-all
```

**Comandos esenciales para desarrollo:**
```bash
# Flujo de desarrollo diario
make dev           # Iniciar servidor de desarrollo
make docs          # Abrir documentación API en navegador
make check-all     # Ejecutar linting, verificación de tipos, y tests
make test          # Ejecutar solo tests
make lint          # Verificar estilo de código
make typecheck     # Verificar tipos con pyrefly

# Flujo Docker
make docker-build  # Construir con tu nombre de servicio
make docker-run    # Ejecutar contenedor localmente
```

## 📋 Patrones Comunes y Ejemplos

### Agregar un Nuevo Servicio Externo

1. **Agregar clase cliente** en `app/clients/external_client.py`
2. **Agregar URL a config** en `app/config.py` y `.env`
3. **Registrar en contenedor DI** en `app/dependencies.py`
4. **Inyectar en servicio** en tu servicio de negocio
5. **Escribir tests** con cliente mockeado

### Manejar Fallos de Servicios Externos

La plantilla muestra cómo manejar fallos graciosamente:

```python
async def robust_external_call(self):
    try:
        result = await self.external_client.get_data()
        return result
    except httpx.HTTPError as e:
        logger.warning("Servicio externo falló", error=str(e))
        return {"error": "Servicio no disponible", "fallback": True}
```

### Agregar Autenticación

```python
# En tu clase cliente
class AuthenticatedClient(BaseClient):
    def __init__(self, http_client: httpx.AsyncClient, base_url: str, api_key: str):
        super().__init__(http_client, base_url)
        self.api_key = api_key

    async def _make_request(self, method: str, endpoint: str, **kwargs):
        headers = kwargs.setdefault("headers", {})
        headers["Authorization"] = f"Bearer {self.api_key}"
        return await super()._make_request(method, endpoint, **kwargs)
```

## 🆘 Solución de Problemas

### Problemas Comunes

1. **UV no encontrado**: Instalar gestor de paquetes UV primero:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   # Luego reiniciar tu terminal o ejecutar: source ~/.bashrc
   ```

2. **Errores de Import**: Asegurar que has ejecutado `make dev-install`
3. **Errores de Tipo**: Ejecutar `make typecheck` para ver problemas de pyrefly
4. **Fallos de Test**: Verificar que todos los servicios externos estén apropiadamente mockeados
5. **Problemas Docker**: Asegurar que existe archivo `.env` y tiene valores correctos
6. **Hooks de pre-commit fallando**: Ejecutar `make pre-commit-install` para configurarlos

### Obtener Ayuda

- Verificar los logs: logging estructurado proporciona información detallada de errores
- Usar el debugger: establecer breakpoints en tu IDE
- Ejecutar tests individualmente: `uv run pytest tests/unit/test_specific.py -v -s`

## 🎓 Próximos Pasos

Una vez que tengas tu microservicio funcionando:

1. **Agregar más endpoints** siguiendo el mismo patrón
2. **Agregar autenticación y autorización** si es necesario
3. **Configurar monitoreo** y alertas
4. **Configurar CI/CD** usando las GitHub Actions incluidas
5. **Desplegar a tu proveedor de nube** usando el contenedor Docker

## 📊 Integración ELK Stack & OpenTelemetry

Esta plantilla incluye observabilidad completa con el stack ELK (Elasticsearch, Logstash, Kibana) y OpenTelemetry para trazabilidad distribuida, logging estructurado y recolección de métricas.

### 🏗️ Arquitectura de Observabilidad

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Aplicación    │───▶│ OpenTelemetry   │───▶│  Elasticsearch  │
│    FastAPI      │    │   Collector     │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
         │                       │                       │
         │              ┌─────────────────┐              │
         └─────────────▶│    Logstash     │──────────────┘
                        │                 │
                        └─────────────────┘
                                 │
                        ┌─────────────────┐
                        │     Kibana      │◀── Dashboard & Visualización
                        │                 │
                        └─────────────────┘
```

### 🚀 Características de Observabilidad

- **Trazabilidad Distribuida**: Seguimiento end-to-end de requests con OpenTelemetry
- **Logging Estructurado**: Logs JSON con correlación de trazas e IDs de request
- **Recolección de Métricas**: Métricas de rendimiento de aplicación y negocio
- **Monitoreo en Tiempo Real**: Dashboards en vivo y visualización en Kibana
- **Agregación de Logs**: Logging centralizado con capacidades de búsqueda potentes
- **Auto-Instrumentación**: Trazabilidad automática de requests HTTP, APIs externas y llamadas a base de datos

### 📋 Stack de Observabilidad

- **OpenTelemetry** - Trazabilidad distribuida y recolección de métricas
- **Elasticsearch** - Motor de búsqueda y analytics para logs y trazas
- **Logstash** - Pipeline de procesamiento y enriquecimiento de logs
- **Kibana** - Plataforma de visualización y dashboards
- **OpenTelemetry Collector** - Procesamiento y exportación de datos de telemetría

### 🔧 Inicio Rápido con ELK Stack

#### Opción 1: Docker Compose (Desarrollo)

1. **Iniciar el stack ELK completo:**
   ```bash
   make elk-up
   ```

2. **Esperar que todos los servicios estén listos** (2-3 minutos):
   ```bash
   # Verificar estado de servicios
   docker-compose -f docker-compose.elk.yml ps

   # Ver logs
   make elk-logs
   ```

3. **Acceder a tu plataforma de observabilidad:**
   - **Aplicación FastAPI**: http://localhost:8000
   - **Documentación API**: http://localhost:8000/docs
   - **Dashboard Kibana**: http://localhost:5601
   - **API Elasticsearch**: http://localhost:9200

#### Opción 2: Kubernetes con Minikube (Tipo Producción)

1. **Desplegar a Minikube con stack ELK completo:**
   ```bash
   make k8s-deploy
   ```

2. **Agregar entradas DNS locales** (como muestra el script de configuración):
   ```bash
   # Agregar a /etc/hosts
   sudo echo "$(minikube ip)    fastapi-app.local" >> /etc/hosts
   sudo echo "$(minikube ip)    kibana.local" >> /etc/hosts
   ```

3. **Acceder a los servicios:**
   - **Aplicación FastAPI**: http://fastapi-app.local
   - **Documentación API**: http://fastapi-app.local/docs
   - **Dashboard Kibana**: http://kibana.local

### 📊 Entendiendo Tus Datos de Observabilidad

#### Trazabilidad de Requests

Cada request automáticamente obtiene:
- **ID Único de Request**: Para correlación a través de todos los logs
- **ID de Traza e ID de Span**: Para trazabilidad distribuida entre servicios
- **Métricas de Rendimiento**: Duración de request, códigos de estado, detalles de errores

Ejemplo de entrada de log estructurado:
```json
{
  "@timestamp": "2024-01-15T10:30:45.123Z",
  "level": "INFO",
  "message": "Request completado",
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

#### Instrumentación Automática

La aplicación automáticamente traza:
- **Requests HTTP entrantes** con detalles completos de request/response
- **Llamadas HTTP salientes** a servicios externos (httpx, requests)
- **Spans de lógica de negocio** con atributos personalizados
- **Seguimiento de errores** con stack traces y contexto

### 🔍 Usando Kibana para Observabilidad

#### Configuración Inicial

1. **Acceder a Kibana**: http://localhost:5601 o http://kibana.local
2. **Crear Patrones de Índice**:
   - Navegar a Stack Management → Index Patterns
   - Crear patrón: `fastapi-logs-*` (para logs de aplicación)
   - Crear patrón: `fastapi-traces-*` (para trazas distribuidas)
   - Crear patrón: `fastapi-metrics-*` (para métricas de aplicación)

#### Consultas de Búsqueda Potentes

**Encontrar todos los errores en la última hora:**
```
level:ERROR AND @timestamp:[now-1h TO now]
```

**Trazar un request específico end-to-end:**
```
request_id:"550e8400-e29b-41d4-a716-446655440000"
```

**Identificar requests lentos (>1000ms):**
```
duration_ms:>1000 AND @timestamp:[now-24h TO now]
```

**Monitorear endpoints API específicos:**
```
path:"/process" AND method:"POST" AND status_code:[400 TO 599]
```

#### Creando Dashboards Operacionales

Construye dashboards completos con:
1. **Tasa de Requests en el Tiempo** - Gráfico de línea mostrando RPS
2. **Percentiles de Tiempo de Respuesta** - Tendencias de latencia P50, P95, P99
3. **Monitoreo de Tasa de Error** - Porcentaje de requests fallidos
4. **Top Endpoints API** - Endpoints más frecuentemente llamados
5. **Distribución de Códigos de Estado** - Desglose 2xx/4xx/5xx
6. **Distribución Geográfica de Requests** - Si se loguean IPs de cliente

### 🛠️ Configuración de Observabilidad

#### Variables de Entorno para Integración ELK

```bash
# Configuración Stack ELK
ELASTICSEARCH_URL=http://localhost:9200
ELASTICSEARCH_INDEX=fastapi-logs

# Configuración OpenTelemetry
OTEL_SERVICE_NAME=fastapi-base-service
OTEL_SERVICE_VERSION=0.1.0
OTEL_EXPORTER_OTLP_ENDPOINT=http://localhost:4318
OTEL_RESOURCE_ATTRIBUTES=service.namespace=microservices,deployment.environment=development

# Switches de Características de Observabilidad
ENABLE_TRACING=true
ENABLE_METRICS=true
ENABLE_LOGGING=true
```

#### Instrumentación Personalizada en Tu Código

Agrega trazabilidad específica de negocio a tus servicios:

```python
from opentelemetry import trace
from app.observability import get_logger

tracer = trace.get_tracer(__name__)
logger = get_logger(__name__)

async def procesar_datos_usuario(user_id: str, data: dict):
    with tracer.start_as_current_span("procesar_datos_usuario") as span:
        # Agregar contexto de negocio a spans
        span.set_attribute("user.id", user_id)
        span.set_attribute("data.size", len(str(data)))

        # Logging estructurado con contexto
        logger.info("Procesando datos de usuario",
                   user_id=user_id,
                   data_type=type(data).__name__)

        try:
            # Tu lógica de negocio aquí
            result = await tu_logica_de_negocio(user_id, data)

            span.set_attribute("processing.status", "success")
            span.set_attribute("result.items_count", len(result))

            return result

        except Exception as e:
            span.record_exception(e)
            span.set_status(trace.Status(trace.StatusCode.ERROR, str(e)))
            logger.error("Fallo al procesar datos de usuario",
                        user_id=user_id, error=str(e))
            raise
```

### 📈 Monitoreo de Producción

#### Métricas Clave para Monitorear

1. **Tasa de Requests (RPS)**: Tendencia de requests por segundo
2. **Tasa de Error**: Porcentaje de respuestas 4xx/5xx
3. **Tiempo de Respuesta**: Latencia percentil 95
4. **Throughput**: Requests exitosos por minuto
5. **Salud del Servicio**: Estado del endpoint de health check
6. **Uso de Recursos**: Utilización de CPU, memoria y disco

#### Configurando Alertas

Crea alertas proactivas en Kibana para:
- **Alta Tasa de Error**: >5% errores en ventana de 5 minutos
- **Tiempos de Respuesta Lentos**: percentil 95 >1000ms
- **Caídas de Tasa de Request**: >50% disminución en tráfico
- **Indisponibilidad del Servicio**: Fallos del health check

### 🧹 Mantenimiento de Observabilidad

#### Gestión de Retención de Datos

Configurar gestión del ciclo de vida de Elasticsearch:

```bash
# Configurar política de retención de 30 días
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

#### Comandos de Observabilidad

```bash
# Gestión Stack ELK (Docker Compose)
make elk-up              # Iniciar stack ELK
make elk-down            # Detener stack ELK
make elk-logs            # Ver logs de todos los servicios

# Despliegue ELK Kubernetes
make k8s-deploy          # Desplegar stack completo a Minikube
make k8s-status          # Verificar estado del despliegue
make k8s-logs            # Ver logs de aplicación
make k8s-cleanup         # Eliminar todos los recursos

# Verificaciones de Salud
curl http://localhost:9200/_cluster/health  # Salud de Elasticsearch
curl http://localhost:8000/health           # Salud de aplicación
```

### 🐛 Solucionando Problemas de Observabilidad

#### Problemas Comunes y Soluciones

**Elasticsearch no inicia:**
```bash
# Aumentar memoria virtual
sudo sysctl -w vm.max_map_count=262144

# Verificar recursos disponibles
docker stats
```

**No aparecen logs en Kibana:**
1. Verificar que existen patrones de índice y coinciden con tus datos
2. Verificar rango de tiempo en Kibana (últimos 15 minutos → últimas 24 horas)
3. Verificar que la aplicación está enviando logs a Elasticsearch:
   ```bash
   curl "localhost:9200/fastapi-logs-*/_search?pretty"
   ```

**Trazas de OpenTelemetry no aparecen:**
1. Verificar logs del OpenTelemetry Collector:
   ```bash
   docker-compose -f docker-compose.elk.yml logs otel-collector
   ```
2. Verificar configuración del endpoint OTLP en la aplicación
3. Asegurar que el patrón de índice de trazas está creado en Kibana

### 🔒 Mejores Prácticas de Seguridad

Para despliegues de producción:

1. **Habilitar Seguridad de Elasticsearch**: Configurar autenticación y TLS
2. **Asegurar Acceso a Kibana**: Implementar autenticación apropiada
3. **Aislamiento de Red**: Usar redes privadas y VPNs
4. **Encriptación de Datos**: Habilitar TLS para toda comunicación inter-servicios
5. **Sanitización de Logs**: Asegurar que no aparezcan datos sensibles en logs
6. **Control de Acceso**: Implementar acceso basado en roles para datos de observabilidad

Esta configuración completa de observabilidad te da capacidades de monitoreo de grado empresarial con configuración mínima. El stack ELK proporciona insights poderosos sobre el comportamiento, rendimiento y salud de tu aplicación, facilitando identificar y resolver problemas rápidamente.

Esta plantilla te da una base sólida sobre la cual construir. Cada componente está diseñado para ser fácilmente extensible y completamente testeable. ¡Feliz programación! 🚀
