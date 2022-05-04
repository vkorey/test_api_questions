import sqlalchemy

from app.db import Base


class Question(Base):
    __tablename__ = "questions"
    id = sqlalchemy.Column(
        sqlalchemy.Integer, primary_key=True, index=True, nullable=False
    )
    question_id = sqlalchemy.Column(
        sqlalchemy.Integer,
        unique=True,
    )
    question_text = sqlalchemy.Column(sqlalchemy.String)
    answer = sqlalchemy.Column(sqlalchemy.String)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime)
