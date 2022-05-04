from pydantic import BaseModel, validator


class QuestionBase(BaseModel):
    amount: int

    @validator("amount")
    def check_amount(cls, v):
        if v <= 0 or v > 100:
            raise ValueError("Amount must be greater than 0 and lower than 100")
        return v
