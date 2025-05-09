"""Pydantic‑схема для объекта user из https://reqres.in"""

from pydantic import BaseModel, HttpUrl, EmailStr, Field


class UserData(BaseModel):
    id: int = Field(gt=0)
    email: EmailStr
    first_name: str
    last_name: str
    avatar: HttpUrl
