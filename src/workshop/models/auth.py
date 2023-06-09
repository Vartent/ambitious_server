from pydantic import BaseModel
from typing import Optional


class BaseUser(BaseModel):
    email: str | None
    username: str


class UserCreate(BaseUser):
    password: str


class User(BaseUser):
    id: int

    class Config:
        orm_mode = True


class Token(BaseModel):
    access_token: str
    token_type: str = 'bearer'
