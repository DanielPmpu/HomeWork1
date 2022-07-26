from fastapi import APIRouter, Depends
from src.services.users import (
    UserService,
    get_current_user,
    get_token,
    get_user_service
)
from src.api.v1.schemas.users import UserModel
from src.api.v1.schemas.auth import Login, Logout, Signup, Tokens
from src.models.user import User


router = APIRouter()


@router.post(
    path="/signup",
    response_model=UserModel,
    summary="Регистрация пользователя",
    tags=["auth"],
)
def signup(
    signup_data: Signup,
    user_service: UserService = Depends(get_user_service)
) -> UserModel:
    user = user_service.create_user(user=signup_data)
    return user


@router.post(
    path="/login",
    response_model=Tokens,
    summary="Авторизация пользователя",
    tags=["auth"],
)
def login(
    login_data: Login,
    user_service: UserService = Depends(get_user_service)
) -> UserModel:
    tokens = user_service.login_user(login_data=login_data)
    return tokens


@router.post(
    path="/refresh",
    response_model=Tokens,
    summary="Обновление токена",
    tags=["auth"],
)
def refresh(
    token: str = Depends(get_token),
    user_service: UserService = Depends(get_user_service),
):
    tokens = user_service.refresh_token(token)
    return tokens


@router.post(
    path="/logout",
    summary="Выход",
    tags=["auth"],
)
def logout(
    logout_data: Logout,
    access_token: str = Depends(get_token),
    user: User = Depends(get_current_user),
    user_service: UserService = Depends(get_user_service),
):
    user_service.logout(user, access_token, logout_data.refresh_token)
    return {'msg': 'You have been logged out.'}


@router.post(
    path="/logout_all",
    summary="Выход со всех устройств",
    tags=["auth"],
)
def logout_all(
    user: User = Depends(get_current_user),
    user_service: UserService = Depends(get_user_service),
):
    user_service.logout_all(user)
    return {'msg': 'You have been logged out from all devices'}
