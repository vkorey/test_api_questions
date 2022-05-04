import pytest
from environs import Env
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import create_database, drop_database

from app.db import Base, get_db
from app.main import app

env = Env()
env.read_env()

DB_USER = env('DB_USER')
DB_PASS = env('DB_PASS')
DB_HOST = env('DB_HOST')
DB_NAME = env('DB_NAME')


TEST_SQLALCHEMY_DATABASE_URL= (
    f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}_test"
)
create_database(TEST_SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    TEST_SQLALCHEMY_DATABASE_URL,
)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()
        drop_database(TEST_SQLALCHEMY_DATABASE_URL)

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)

def test_health_check():
    response = client.post("/question", json={"amount":5})
    assert response.status_code == 200


