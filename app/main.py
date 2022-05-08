from fastapi import FastAPI

from app import models
from app.db import engine
from app.routers import router

models.Base.metadata.create_all(bind=engine)

description = """
API Questions

## question

Получить последний сохранненый вопрос из базы данных
"""

app = FastAPI(
    title="API Questions",
    description=description,
)

app.include_router(router)
