from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routers import tables
from .auth import auth_users
from .settings import STATIC_FOLDER_IMAGES


app = FastAPI()

app.include_router(auth_users.router, prefix='/users',
                   tags=["users"])
app.include_router(tables.router, prefix='/libraries',
                   tags=["libraries"])
app.include_router(tables.router, prefix='/museums',
                   tags=["museums"])
app.include_router(tables.router, prefix='/cemeteries',
                   tags=["cemeteries"])
app.include_router(tables.router, prefix='/educational-centers',
                   tags=["educational-centers"])
app.include_router(tables.router, prefix='/fire-stations',
                   tags=["fire-stations"])
app.include_router(tables.router, prefix='/monuments',
                   tags=["monuments"])
app.include_router(tables.router, prefix='/municipal-swimming-pools',
                   tags=["municipal-swimming-pools"])
app.include_router(tables.router, prefix='/parks',
                   tags=["parks"])
app.include_router(tables.router, prefix='/police-stations',
                   tags=["police-stations"])
app.include_router(tables.router, prefix='/public-schools',
                   tags=["public-schools"])
app.include_router(tables.router, prefix='/public-parkings',
                   tags=["public-parkings"])
app.include_router(tables.router, prefix='/recycling-points',
                   tags=["recycling-points"])

app.mount('/static/images', StaticFiles(directory=f'/code/{STATIC_FOLDER_IMAGES}'), name='images')
