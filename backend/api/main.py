from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routers import collections, users


app = FastAPI()

app.include_router(users.router, prefix='/users')
app.include_router(collections.router, prefix='/libraries')
app.include_router(collections.router, prefix='/museums')
app.include_router(collections.router, prefix='/cemeteries')
app.include_router(collections.router, prefix='/educational-centers')
app.include_router(collections.router, prefix='/fire-stations')
app.include_router(collections.router, prefix='/monuments')
app.include_router(collections.router, prefix='/municipal-swimming-pools')
app.include_router(collections.router, prefix='/parks')
app.include_router(collections.router, prefix='/police-stations')
app.include_router(collections.router, prefix='/public-schools')
app.include_router(collections.router, prefix='/public-parkings')
app.include_router(collections.router, prefix='/recycling-points')

app.mount('/static/images', StaticFiles(directory='/code/backend/static/images'), name='images')
