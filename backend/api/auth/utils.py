from datetime import datetime, timedelta
from typing import Optional


from fastapi import Depends, HTTPException, status, Request
from jose import jwt, JWTError
from passlib.context import CryptContext

from api.crud import search_element_in_db
from api.settings import auth_settings
from backend.db.schemas import model_schema
from db.models import User
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.utils import get_authorization_scheme_param


class CustomOAuth2PasswordBearer(OAuth2PasswordBearer):
    async def __call__(self, request: Request) -> Optional[str]:
        authorization = request.headers.get("Authorization")
        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail='Usuario no autenticado',
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None
        return param


oauth2 = CustomOAuth2PasswordBearer(tokenUrl="login")
collection = 'users'

ACCESS_TOKEN_DURATION = 30

password_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def get_token(user):
    access_token = {
        'sub': user.username,
        'exp': datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)
    }
    return {'access_token': jwt.encode(access_token,
                                       key=auth_settings._secret,
                                       algorithm=auth_settings._algorithm), 'token_type': 'bearer'}


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)


def authenticate_user(user):
    user_in_db = search_element_in_db(collection, 'name', user.username)
    if user_in_db:
        if not user_in_db['is_active']:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail='Usuario inactivo o eliminado')
        if verify_password(user.password, user_in_db['password']):
            return True
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                        detail='Usuario o contraseña incorrecta')


def validate_new_user(name, password, password_confirm):
    if search_element_in_db(collection, 'name', name):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail='El usuario ya existe')
    if password != password_confirm:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail='Los passwords no coinciden')
    return True


def authenticated_user(token: str = Depends(oauth2)):
    try:
        username = jwt.decode(token,
                              key=auth_settings._secret,
                              algorithms=auth_settings._algorithm).get('sub')
        if username:
            user = search_element_in_db(collection, 'name', username)
            return model_schema(collection, user)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Credenciales invalidas',
                            headers={'WWW-Authenticate': 'Bearer'})


def authenticated_admin(token: str = Depends(oauth2)):
    try:
        username = jwt.decode(token,
                              key=auth_settings._secret,
                              algorithms=auth_settings._algorithm).get('sub')
        if username:
            user = search_element_in_db(collection, 'name', username)
            if not user['is_admin']:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                    detail='Credenciales invalidas')
            return model_schema(collection, user)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail='Credenciales invalidas',
                            headers={'WWW-Authenticate': 'Bearer'})
