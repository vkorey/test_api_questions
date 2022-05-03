from pydantic import BaseModel, validator


class Question(BaseModel):
    amount: int

    @validator("amount")
    def check_amount(cls, v):
        if v > 100:
            raise ValueError("Amount must be lower than 100")
        return v
