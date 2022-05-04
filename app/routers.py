
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas import QuestionBase
from app.utils import check_and_store, get_questions

router = APIRouter()


@router.post('/question')
async def question(
    question: QuestionBase,
    db: Session = Depends(get_db)
):
    response = get_questions(question.amount)
    check_and_store(response, question.amount, db)
