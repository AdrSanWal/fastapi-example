from bson import ObjectId
from bson.errors import InvalidId
from typing import List

from fastapi import APIRouter, status, Response, HTTPException

from ..db.client import client
from ..db.models import User
from ..db.schemas import user_schema

router = APIRouter(prefix='/users')


def search_user(field: str, value: str | ObjectId):
    try:
        user = client.db.users.find_one({field: value})
        return user_schema(user)
    except AttributeError:
        return None


@router.get("/")
async def users() -> List:
    users = client.db.users.find()
    return [user_schema(_) for _ in users]


@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_user(user: User):
    user = user.dict(exclude={'id'})
    id = client.db.users.replace_one(user, user, upsert=True).upserted_id
    user = search_user("_id", id)
    if user:
        return user
    raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                        detail="User alredy exists")


@router.get("/{id}")
async def get_user(id: str):
    user = search_user("_id", ObjectId(id))
    if user:
        return user
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="User not exists")


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(id: str):
    client.db.users.delete_one({"_id": ObjectId(id)})


@router.put("/")
async def put_user(user: User):
    try:
        client.db.users.find_one_and_replace({"_id": ObjectId(user.id)},
                                             user.dict(exclude={'id'}))
        user = search_user("_id", ObjectId(user.id))
        return user

    except InvalidId:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Id not found")
