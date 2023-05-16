from bson import ObjectId
from bson.errors import InvalidId
from typing import List

from fastapi import status, HTTPException

from db.client import client
from db.schemas import model_schema
from api.settings import settings


def search_element_in_db(collection: str, field: str, value: str | ObjectId):
    try:
        user = client[settings._db][collection].find_one({field: value})
        return user
    except AttributeError:
        return None


def id_is_valid_ObjectId(id: str):
    """Attempts to convert a string to an ObjectId.
    If it can't, raise an exception.
    """
    try:
        id = ObjectId(id)
        return id
    except InvalidId:
        e = f"{id} no es un ObjectId válido, debe ser un input (12-byte) o" \
            + " una cadena hexadecimal (24-character)"
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail=e)


async def get_all(collection: str):
    """Given a collection, tries to return all the elements it contains."""
    elements = client[settings._db][collection].find()
    print(settings._db, collection)
    return [model_schema(collection, _) for _ in elements]


async def post_instance(collection: str, instance):
    """Given a collection, tries to insert a document into it."""
    instance = instance.dict(exclude={'id'})
    id = client[settings._db][collection].replace_one(instance,
                                                      instance,
                                                      upsert=True).upserted_id
    element = search_element_in_db(collection, "_id", id)

    if element:
        return model_schema(collection, element)

    raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                        detail=f"La instancia ya existe en {collection}")


async def get_instance(collection: str, id: str):
    """Given a collection, returns a document by it's id."""
    id = id_is_valid_ObjectId(id)
    element = search_element_in_db(collection, "_id", id)

    if element:
        return model_schema(collection, element)
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="La instancia no existe")


async def delete_instance(collection: str, id: str):
    """Given a collection, delete a document by it's id."""
    id = id_is_valid_ObjectId(id)
    client[settings._db][collection].delete_one({"_id": id})


async def put_instance(collection: str, id: str, instance):
    """Given a collection, update a document by it's id."""
    id = id_is_valid_ObjectId(id)
    client[settings._db][collection].find_one_and_replace({"_id": id},
                                                          instance.dict(exclude={'id'}))
    element = search_element_in_db(collection, "_id", id)

    if element:
        return model_schema(collection, element)
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                        detail="No se ha encontrado el Id")
