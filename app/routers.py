from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.db_utils import DButils
from app.schemas import QuestionBase
from app.utils import get_questions

router = APIRouter()


@router.post("/question")
async def question(question: QuestionBase, db: Session = Depends(get_db)):
    pers = DButils(db)
    result = pers.get_last_question()
    response = await get_questions(question.amount)
    if response is None:
        return result
    await pers.check_and_store(response, question.amount)
    return result
