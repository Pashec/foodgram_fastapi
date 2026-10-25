from fastapi import APIRouter
from core.config import settings
from api.endpoints.health import router as health_router


main_router = APIRouter(prefix=settings.api_prefix)

main_router.include_router(
    health_router,
    prefix='/health',
    tags=['Health'],
)