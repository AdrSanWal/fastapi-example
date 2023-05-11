from typing import List

from fastapi import APIRouter, status, Request

from .crud import get_all, post_instance, get_instance, delete_instance, put_instance
from db.models import Model


router = APIRouter()


def get_collection_from_url(request: Request):
    collection = str(request.url).split('/')
    return collection[-2]


@router.get("/")
async def get_elements(request: Request) -> List:
    collection = get_collection_from_url(request)
    return await get_all(collection)


@router.post("/", status_code=status.HTTP_201_CREATED)
async def post_element(model: Model, request: Request):
    collection = get_collection_from_url(request)
    return await post_instance(collection, model)


@router.get("/{id}")
async def get_element(id: str, request: Request):
    collection = get_collection_from_url(request)
    return await get_instance(collection, id)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_element(id: str, request: Request):
    collection = get_collection_from_url(request)
    await delete_instance(collection, id)


@router.put("/{id}")
async def put_element(id: str, model: Model, request: Request):
    collection = get_collection_from_url(request)
    return await put_instance(collection, id, model)
