from os import path
from shutil import copyfileobj
from typing import Annotated, List, Optional

from fastapi import APIRouter, Depends, Form, UploadFile, status
from fastapi.security import OAuth2PasswordRequestForm

from api import crud
from db.models import DBUser, User
from . import utils


collection = 'users'

router = APIRouter()


async def store_image(image):
    static_image = f'backend/static/images/{image.filename}'
    file_object = image.file
    with open(static_image, "wb") as buffer:
        copyfileobj(file_object, buffer)

    return image.filename


@router.get("/")
async def users(user: User = Depends(utils.authenticated_admin)) -> List:
    return await crud.get_all(collection)


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def post_user(name: Annotated[str, Form()],
                    surname: Annotated[str, Form()],
                    age: Annotated[int, Form()],
                    password: Annotated[str, Form()],
                    password_confirm: Annotated[str, Form()],
                    is_active: Annotated[bool, Form()] = True,
                    is_admin: Annotated[bool, Form()] = False,
                    image: Optional[UploadFile] = None):

    if utils.validate_new_user(name, password, password_confirm):
        hashed_password = utils.get_hashed_password(password)
        user = DBUser(name=name,
                      password=hashed_password,
                      surname=surname,
                      age=age,
                      is_active=is_active,
                      is_admin=is_admin)
        if image:
            user.image = await store_image(image)
        return await crud.post_instance(collection, user)


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(form: OAuth2PasswordRequestForm = Depends()):
    if utils.authenticate_user(form):
        token = utils.get_token(form)
        return token


@router.get("/me", status_code=status.HTTP_200_OK)
async def me(user: User = Depends(utils.authenticated_user)):
    return user


@router.get("/{id}")
async def get_user(id: str, user: User = Depends(utils.authenticated_admin)):
    return await crud.get_instance(collection, id)


# @router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_user(id: str):
#     await delete_instance(collection, id)


# @router.put("/{id}")
# async def put_user(id: str, user: User):
#     return await put_instance(collection, id, user)
