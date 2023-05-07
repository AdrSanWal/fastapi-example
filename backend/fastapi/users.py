from pydantic import BaseModel

from fastapi import APIRouter

router = APIRouter()


class User(BaseModel):
    name: str
    surname: str
    url: str
    age: int



@router.get("/users")
async def users():
    return "!Hola Mundo!"
