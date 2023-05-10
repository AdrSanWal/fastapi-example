from fastapi import FastAPI

from .settings import Settings
from . import users


app = FastAPI()

app.include_router(users.router)
