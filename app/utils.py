
import requests

from app.models import Question


def get_questions(amount: int):
    headers = {}
    payload = {}
    url = "https://jservice.io/api/random?count=" + str(amount)
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()


def is_unique_question(
    question_id: int,
    db
):
    question = db.query(Question).filter(
        Question.question_id == question_id
    ).first()
    if not question:
        return True


def save_question(
    db,
    question_id: int,
    question: str,
    answer: str,
    created_at: str
):
    q = Question(
        question_id=question_id,
        question_text=question,
        answer=answer,
        created_at=created_at
    )
    db.add(q)
    db.commit()


def check_and_store(response: dict, amount: int, db):
    for question in range(amount):
        if is_unique_question(response[question]['id'], db):
            question_id = response[question]['id']
            question_text = response[question]['question']
            answer = response[question]['answer']
            created_at = response[question]['created_at']
            save_question(
                db,
                question_id,
                question_text,
                answer,
                created_at
            )
        else:
            new_response = get_questions(1)
            check_and_store(new_response, 1, db)
