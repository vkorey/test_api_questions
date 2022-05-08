from environs import Env
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

env = Env()
env.read_env()

DB_USER = env("DB_USER")
DB_PASS = env("DB_PASS")
DB_HOST = env("DB_HOST")
DB_NAME = env("DB_NAME")
SQLALCHEMY_DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:5432/{DB_NAME}"
)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
