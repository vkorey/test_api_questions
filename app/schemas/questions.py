from datetime import datetime
from typing import Optional
from pydantic import BaseModel, validator

class Question(BaseModel):
    questions_num: int

    @validator("amount")
    def check_amount(cls, v):
        if v >= 1000:
            raise ValueError("Amount must be lower than 100")
        return v

