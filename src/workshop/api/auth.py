from fastapi import APIRouter, Depends, Response

from fastapi.security import OAuth2PasswordRequestForm
from ..models.auth import (
    User,
    UserCreate,
    Token
)
from ..services.auth import AuthService, get_current_user

router = APIRouter(
    prefix='/auth'
)


@router.post('/sing-up', response_model=Token)
def sing_up(
        user_data: UserCreate,
        service: AuthService = Depends()):
    return service.register_new_user(user_data)


@router.post('/sing-in')
def sing_in(
        response: Response,
        form_data: OAuth2PasswordRequestForm = Depends(),
        service: AuthService = Depends()):
    token = service.authenticate_user(
            form_data.username,
            form_data.password
    )
    response.set_cookie(
        key="access_token",
        value=token.access_token)
    return token


@router.get('/user', response_model=User)
def get_user(user: User = Depends(get_current_user)):
    return user


@router.get('/get-test')
def get_test():
    return {'test': 'hello world'}
