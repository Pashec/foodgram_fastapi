from fastapi import APIRouter
from core.config import settings

from api.endpoints.health import router as health_router
from api.endpoints.tags import router as tags_router
from api.endpoints.ingredients import router as ingredients_router

main_router = APIRouter(prefix=settings.api_prefix)

main_router.include_router(health_router, prefix='/health', tags=['Health'])
main_router.include_router(tags_router, prefix='/tags', tags=['Tags'])
main_router.include_router(ingredients_router, prefix='/ingredients', tags=['Ingredients'])
