from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from api.routers import main_router

# Инициализаия приложения фастапи
app = FastAPI(title=settings.app_title)

# Настройки CROS
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# Подключение роутера
app.include_router(main_router)


