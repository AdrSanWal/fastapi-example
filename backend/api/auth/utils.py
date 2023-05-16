from datetime import datetime, timedelta
from typing import Optional

from fastapi import Depends, HTTPException, status, Request
from fastapi.param_functions import Form
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.utils import get_authorization_scheme_param
from jose import jwt, JWTError
from passlib.context import CryptContext

from api.crud import search_element_in_db
from api.settings import auth_settings
from backend.db.schemas import model_schema
from db.models import User
from api import error_msg


class CustomOAuth2PasswordRequestForm:
    """Email and password request Form"""
    def __init__(
        self,
        grant_type: str = Form(default=None, regex="password"),
        email: str = Form(),
        password: str = Form(),
        scope: str = Form(default=""),
        client_id: Optional[str] = Form(default=None),
        client_secret: Optional[str] = Form(default=None),
    ):
        self.grant_type = grant_type
        self.email = email
        self.password = password
        self.scopes = scope.split()
        self.client_id = client_id
        self.client_secret = client_secret


class CustomOAuth2PasswordBearer(OAuth2PasswordBearer):
    async def __call__(self, request: Request) -> Optional[str]:
        authorization = request.headers.get("Authorization")
        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail=error_msg.not_auth_user,
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
        'sub': user.email,
        'exp': datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)
    }
    return {'access_token': jwt.encode(access_token,
                                       key=auth_settings.secret,
                                       algorithm=auth_settings.algorithm), 'token_type': 'bearer'}


def get_hashed_password(password: str) -> str:
    return password_context.hash(password)


def verify_password(password: str, hashed_pass: str) -> bool:
    return password_context.verify(password, hashed_pass)


def authenticate_user(user):
    user_in_db = search_element_in_db(collection, 'email', user.email)
    if user_in_db:
        if not user_in_db['is_active']:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                                detail=error_msg.user_inactive)
        if verify_password(user.password, user_in_db['password']):
            return True
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
                        detail=error_msg.login_fail)


def validate_new_user(email, password, password_confirm):
    if search_element_in_db(collection, 'email', email):
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail=error_msg.user_already_exists)
    if password != password_confirm:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=error_msg.diferent_passwords)
    return True


def authenticated_user(token: str = Depends(oauth2)):
    try:
        email = jwt.decode(token,
                           key=auth_settings.secret,
                           algorithms=auth_settings.algorithm).get('sub')
        if email:
            user = search_element_in_db(collection, 'email', email)
            return model_schema(collection, user)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=error_msg.invalid_credentials,
                            headers={'WWW-Authenticate': 'Bearer'})


def authenticated_admin(token: str = Depends(oauth2)):
    try:
        email = jwt.decode(token,
                           key=auth_settings.secret,
                           algorithms=auth_settings.algorithm).get('sub')
        if email:
            user = search_element_in_db(collection, 'email', email)
            if not user['is_admin']:
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                    detail=error_msg.invalid_credentials)
            return model_schema(collection, user)
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail=error_msg.invalid_credentials,
                            headers={'WWW-Authenticate': 'Bearer'})
