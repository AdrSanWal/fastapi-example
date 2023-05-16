from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from .routers import tables
from .auth import auth_users


app = FastAPI()

app.include_router(auth_users.router, prefix='/users')
app.include_router(tables.router, prefix='/libraries')
app.include_router(tables.router, prefix='/museums')
app.include_router(tables.router, prefix='/cemeteries')
app.include_router(tables.router, prefix='/educational-centers')
app.include_router(tables.router, prefix='/fire-stations')
app.include_router(tables.router, prefix='/monuments')
app.include_router(tables.router, prefix='/municipal-swimming-pools')
app.include_router(tables.router, prefix='/parks')
app.include_router(tables.router, prefix='/police-stations')
app.include_router(tables.router, prefix='/public-schools')
app.include_router(tables.router, prefix='/public-parkings')
app.include_router(tables.router, prefix='/recycling-points')

app.mount('/static/images', StaticFiles(directory='/code/backend/static/images'), name='images')
