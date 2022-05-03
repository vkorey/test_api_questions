import sqlalchemy

from app.db import Base


class Question(Base):
    __tablename__ = 'questions'
    question_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        unique=True,
        primary_key=True
    )
    question_text = sqlalchemy.Column(sqlalchemy.String, unique=True)
    answer = sqlalchemy.Column(sqlalchemy.String)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime)
