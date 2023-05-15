from os import PathLike
from pydantic import BaseModel
from typing import Union


class User(BaseModel):
    id: str | None
    image: str = 'default.jpg'
    name: str
    surname: str
    age: int


class Location(BaseModel):
    lat: float
    lng: float


class Address(BaseModel):
    locality: str
    postal_code: str
    street: str


class Organization(BaseModel):
    name: str
    description: str
    schedule: str | None  # horario
    services: str | None


class Model(BaseModel):
    id: str | None
    model: str
    title: str
    relation: str  # link
    address: Address
    location: Location
    organization: Organization
