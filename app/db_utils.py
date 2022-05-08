from app.models import Question
from app.utils import get_questions


class DButils():
    def __init__(self, db):
        self.db = db

    def _is_unique_question(self, question_id: int) -> bool:
        question = self.db.query(Question).filter(
            Question.question_id == question_id
        ).first()
        if not question:
            return True

    def _save_question(
        self,
        question_id: int,
        question: str,
        answer: str,
        created_at: str
    ) -> None:
        q = Question(
            question_id=question_id,
            question_text=question,
            answer=answer,
            created_at=created_at,
        )
        self.db.add(q)
        self.db.commit()

    async def check_and_store(self, response: dict, amount: int) -> None:
        for question in range(amount):
            if self._is_unique_question(response[question]["id"]):
                question_id = response[question]["id"]
                question_text = response[question]["question"]
                answer = response[question]["answer"]
                created_at = response[question]["created_at"]
                self._save_question(
                    question_id,
                    question_text,
                    answer,
                    created_at
                )
            else:
                new_response = get_questions(1)
                self.check_and_store(new_response, 1)

    def get_last_question(self) -> dict:
        obj = self.db.query(Question).order_by(Question.id.desc()).first()
        if not obj:
            return {}
        return {
            "id": obj.question_id,
            "question": obj.question_text,
            "answer": obj.answer,
            "created_at": obj.created_at,
        }
