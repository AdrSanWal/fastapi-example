from os import path
from shutil import copyfileobj
from typing import Annotated, List, Optional

from fastapi import APIRouter, Form, UploadFile, status

from api.crud import get_all, post_instance, get_instance, delete_instance, put_instance
from db.models import User


collection = 'users'

router = APIRouter()


async def store_image(image):
    static_image = f'backend/static/images/{image.filename}'
    file_object = image.file
    with open(static_image, "wb") as buffer:
        copyfileobj(file_object, buffer)

    return image.filename


@router.get("/")
async def users() -> List:
    return await get_all(collection)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_user(name: Annotated[str, Form()],
                    surname: Annotated[str, Form()],
                    age: Annotated[int, Form()],
                    image: Optional[UploadFile] = None):

    user = User(name=name, surname=surname, age=age)
    if image:
        user.image = await store_image(image)
    return await post_instance(collection, user)


@router.get("/{id}")
async def get_user(id: str):
    return await get_instance(collection, id)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: str):
    await delete_instance(collection, id)


@router.put("/{id}")
async def put_user(id: str, user: User):
    return await put_instance(collection, id, user)
