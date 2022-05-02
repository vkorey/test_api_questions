
from app.db import database
from app.models.questions import questions_table
from app.schemas import questions as questions_schema



def get_questions(amount: int):
    pass


async def is_unique_question(question_id: int):
    query = questions_table.select().where(
        questions_table.c.question_id == question_id
    )
    await database.fetch_one(query)