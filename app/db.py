from os import environ

from databases import Database

"""DB_USER = environ.get('DB_USER', 'root')
DB_PASSWORD = environ.get('DB_PASS', 'root')
DB_HOST = environ.get('DB_HOST', 'localhost')
DB_NAME = environ.get('DB_NAME', 'questions')"""
SQLALCHEMY_DATABASE_URI  = (
    "postgresql://root:root@localhost:5432/questions"
)

database = Database(SQLALCHEMY_DATABASE_URI)
