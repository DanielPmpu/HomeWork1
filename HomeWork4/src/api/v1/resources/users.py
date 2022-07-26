from fastapi import APIRouter, Depends
from src.api.v1.schemas.users import UserModel, UserUpdate
from src.services.users import UserService, get_current_user, get_user_service
from src.models.user import User


router = APIRouter()


@router.get(
    path="/me",
    response_model=UserModel,
    summary="Просмотр информации о себе",
    tags=["users"],
)
def get_user(
    user: User = Depends(get_current_user),
):
    return user


@router.patch(
    path="/me",
    response_model=UserModel,
    summary="Обновляет информацию о себе",
    tags=["users"],
)
def update_user(
    user_update: UserUpdate,
    user: User = Depends(get_current_user),
    user_service: UserService = Depends(get_user_service),
):
    return user_service.update_user(user, user_update)
