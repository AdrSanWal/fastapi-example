from typing import List

from fastapi import APIRouter, status

from .crud import get_all, post_instance, get_instance, delete_instance, put_instance
from ..db.models import User


router = APIRouter(prefix='/users')

collection = 'users'


@router.get("/")
async def users() -> List:
    return await get_all(collection)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_user(user: User):
    return await post_instance(collection, user)


@router.get("/{id}")
async def get_user(id: str):
    return await get_instance(collection, id)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: str):
    delete_instance(collection, id)


@router.put("/{id}")
async def put_user(id: str, user: User):
    return await put_instance(collection, id, user)
