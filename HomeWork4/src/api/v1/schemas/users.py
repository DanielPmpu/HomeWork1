from datetime import datetime
from typing import Optional
from pydantic import BaseModel


__all__ = ("UserModel",)


class UserModel(BaseModel):
    id: Optional[int]
    email: str
    username: str
    created_at: datetime


class UserUpdate(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
