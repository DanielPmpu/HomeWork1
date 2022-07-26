from pydantic import BaseModel


__all__ = (
    "Signup",
    "Login",
    "Tokens",
)


class Signup(BaseModel):
    username: str
    email: str
    password: str


class Login(BaseModel):
    username: str
    password: str


class Tokens(BaseModel):
    access_token: str
    refresh_token: str


class Logout(BaseModel):
    refresh_token: str
