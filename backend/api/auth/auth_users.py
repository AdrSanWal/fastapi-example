from datetime import datetime
from os import path, remove
from shutil import copyfileobj
from typing import Annotated, List, Optional

from fastapi import APIRouter, Depends, Form, UploadFile, status

from api import crud
from api.settings import STATIC_FOLDER_IMAGES
from db.models import DBUser, User
from . import utils


collection = 'users'

router = APIRouter()


def delete_image(filename):
    image = f'{STATIC_FOLDER_IMAGES}/{filename}'
    if path.exists(image):
        remove(image)


async def store_image(image):
    timestamp_image = f'{datetime.now()}-{image.filename}'
    static_image = f'{STATIC_FOLDER_IMAGES}/{timestamp_image}'
    file_object = image.file
    with open(static_image, "wb") as buffer:
        copyfileobj(file_object, buffer)

    return timestamp_image


@router.get("/")
async def users(user: User = Depends(utils.authenticated_admin)) -> List:
    return await crud.get_all(collection)


@router.post("/signup", status_code=status.HTTP_201_CREATED)
async def post_user(email: Annotated[str, Form()],
                    name: Annotated[str, Form()],
                    surname: Annotated[str, Form()],
                    age: Annotated[int, Form()],
                    password: Annotated[str, Form()],
                    password_confirm: Annotated[str, Form()],
                    is_active: Annotated[bool, Form()] = True,
                    is_admin: Annotated[bool, Form()] = False,
                    image: Optional[UploadFile] = None):

    if utils.validate_new_user(email, password, password_confirm):
        hashed_password = utils.get_hashed_password(password)
        user = DBUser(email=email,
                      name=name,
                      password=hashed_password,
                      surname=surname,
                      age=age,
                      is_active=is_active,
                      is_admin=is_admin)
        if image:
            user.image = await store_image(image)
        return await crud.post_instance(collection, user)


@router.post("/login", status_code=status.HTTP_200_OK)
async def login(form: utils.CustomOAuth2PasswordRequestForm = Depends()):
    if utils.authenticate_user(form):
        token = utils.get_token(form)
        return token


@router.get("/me", status_code=status.HTTP_200_OK)
async def me(user: User = Depends(utils.authenticated_user)):
    return user


@router.delete("/me", status_code=status.HTTP_204_NO_CONTENT)
async def delete_me(user: User = Depends(utils.authenticated_user)):
    await crud.delete_instance(collection, user.id)


@router.put("/me")
async def put_user(name: Annotated[str, Form()],
                   surname: Annotated[str, Form()],
                   age: Annotated[int, Form()],
                   image: Optional[UploadFile] = None,
                   user: User = Depends(utils.authenticated_user)):

    updated_user = User(email=user.email,
                        name=name,
                        surname=surname,
                        image=user.image,
                        age=age,
                        is_active=user.is_active,
                        is_admin=user.is_admin)

    if image and image.filename != user.image:
        updated_user.image = await store_image(image)
        delete_image(user.image)

    return await crud.put_instance(collection, user.id, updated_user)


@router.get("/{id}")
async def get_user(id: str, user: User = Depends(utils.authenticated_admin)):
    return await crud.get_instance(collection, id)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: str, user: User = Depends(utils.authenticated_admin)):
    await crud.delete_instance(collection, id)
