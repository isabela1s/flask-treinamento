from typing import Literal
from pydantic import BaseModel, Field, EmailStr, model_validator

from common.hash import hashpw

class UserCreatePayload(BaseModel):
    name: str = Field(min_length=5, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8)
    age: int = Field(gt=0, lt=120)
    role: Literal["ADMIN", "USER"]

    @model_validator(mode='after')
    def hash_password(self):
        self.password = hashpw(self.password)
        return self