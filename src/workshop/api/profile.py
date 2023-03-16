from fastapi import APIRouter, Depends, Response
from starlette import status

from ..models.profile import (
    ProfileCreate,
    ProfileUpdate
)

from ..models.auth import User

from ..services.profile import ProfileService

from ..services.auth import get_current_user

router = APIRouter(prefix='/profile')


@router.get('/')
def get_profile_current(
        user: User = Depends(get_current_user),
        service: ProfileService = Depends()
):
    return service.get(user.id)


@router.get('/{user_id}')
def get_profile_by_id(
        user_id: int,
        service: ProfileService = Depends()
):
    return service.get(user_id)


@router.post('/{user_id}')
def create_user_profile(
        user_id: int,
        profile_data: ProfileCreate,
        service: ProfileService = Depends()
):
    return service.create(user_id, profile_data)


@router.post('/update/{user_id}')
def update_profile(
        user_id: int,
        profile_data: ProfileUpdate,
        service: ProfileService = Depends()
):
    return service.update(user_id, profile_data)


@router.delete('/{user_id}')
def delete_profile(
        user_id: int,
        service: ProfileService = Depends()
):
    service.delete(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
