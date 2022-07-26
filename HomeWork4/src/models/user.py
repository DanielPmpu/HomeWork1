from datetime import datetime
from typing import Optional
from sqlalchemy import Column, String

from sqlmodel import Field, SQLModel


__all__ = ("User",)


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    email: str = Field(sa_column=Column(
        "email",
        String,
        unique=True,
        nullable=False
    ))
    username: str = Field(sa_column=Column(
        "username",
        String,
        unique=True,
        nullable=False
    ))
    password_hash: str = Field(nullable=False)
    created_at: datetime = Field(default=datetime.utcnow(), nullable=False)
