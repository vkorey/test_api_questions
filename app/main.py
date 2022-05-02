from fastapi import FastAPI

from .routers import question

app = FastAPI()

app.include_router(question.router)
