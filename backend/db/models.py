from pydantic import BaseModel


class User(BaseModel):
    id: str | None
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
    model: str
    title: str
    relation: str  # link
    address: Address
    location: Location
    organization: Organization
