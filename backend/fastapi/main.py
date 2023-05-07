from fastapi import FastAPI

from . import users

app = FastAPI()

app.include_router(users.router)
