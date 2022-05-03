
from fastapi import APIRouter, Depends

from app.db import Session, get_db
from app.schemas import Question
from app.utils import check_and_store, get_questions

router = APIRouter()


@router.post('/question')
async def question(
    question: Question,
    db: Session = Depends(get_db)
):
    response = get_questions(question.amount)
    check_and_store(response, question.amount, db)
