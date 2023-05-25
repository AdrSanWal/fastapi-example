from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from .routers import tables
from .auth import auth_users
from .settings import STATIC_FOLDER_IMAGES
from .routers.utils import get_collections_names


origins = [
    "http://localhost:5173",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount('/static/images', StaticFiles(directory=f'/code/{STATIC_FOLDER_IMAGES}'), name='images')

@app.get("/services")
def get_collections():
    collections = get_collections_names()
    return collections

app.include_router(auth_users.router, prefix='/users',
                   tags=["users"])
app.include_router(tables.router, prefix='/aparcamientos-publicos-municipales',
                   tags=["aparcamientos-publicos-municipales"])
app.include_router(tables.router, prefix='/bibliotecas',
                   tags=["bibliotecas"])
app.include_router(tables.router, prefix='/cementerios',
                   tags=["cementerios"])
app.include_router(tables.router, prefix='/centros-educativos',
                   tags=["centros-educativos"])
app.include_router(tables.router, prefix='/colegios-publicos',
                   tags=["colegios-publicos"])
app.include_router(tables.router, prefix='/comisarias',
                   tags=["comisarias"])
app.include_router(tables.router, prefix='/monumentos',
                   tags=["monumentos"])
app.include_router(tables.router, prefix='/museos',
                   tags=["museos"])
app.include_router(tables.router, prefix='/parques-de-bomberos',
                   tags=["parques-de-bomberos"])
app.include_router(tables.router, prefix='/parques',
                   tags=["parques"])
app.include_router(tables.router, prefix='/piscinas-municipales',
                   tags=["piscinas-municipales"])
app.include_router(tables.router, prefix='/polideportivos',
                   tags=["polideportivos"])
app.include_router(tables.router, prefix='/puntos-limpios',
                   tags=["puntos-limpios"])
app.include_router(tables.router, prefix='/embajadas-y-consulados',
                   tags=["embajadas-y-consulados"])
app.include_router(tables.router, prefix='/parques-y-jardines',
                   tags=['parques-y-jardines'])
app.include_router(tables.router, prefix='/mercados-municipales',
                   tags=['mercados-municipales'])
app.include_router(tables.router, prefix='/puntos-informacion-turistica',
                   tags=['puntos-informacion-turistica'])
