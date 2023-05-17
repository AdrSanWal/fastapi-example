# fastapi-example

Este repositorio es un CRUD de ejemplo con FastAPI, utilizando MongoDB como
base de datos y desplegandolo mediante docker-compose.

Recopila distintos servicios existentes en la comunidad de Madrid.

Instrucciones:
=

1º Clona el repositorio en una carpeta:

    git clone https://github.com/AdrSanWal/fastapi-example.git


2º Ejecuta docker-compose en la carpeta fastapi-example:

    docker-compose up -d

3º Rellena la base de datos con algunos ejemplos:

    docker exec fastapi python3 db/filldb/get_info.py

Documentación:
=

    http://localhost:8000/docs

    http://localhost:8000/redoc

Datos:
=

Ahora mismo los servicios almacenados son:

  -Cementerios
  -Centros de enseñanza
  -Parques de bomberos
  -Librerías
  -Monumentos
  -Piscinas municipales
  -Museos
  -Parques
  -Comisarías
  -Parkings públicos
  -Colegios públicos
  -Puntos limpios
  -Polideportivos

  Si quieres incorporar más sevicios a la base de datos, descarga el json
  correspondiente de la API de datos abiertos de la comunidad de madrid:

  https://datos.madrid.es/portal/site/egob/menuitem.214413fe61bdd68a53318ba0a8a409a0/?vgnextoid=b07e0f7c5ff9e510VgnVCM1000008a4a900aRCRD&vgnextchannel=b07e0f7c5ff9e510VgnVCM1000008a4a900aRCRD&vgnextfmt=default

  Guardalo en backend/db/filldb y vuelve a ejecutar los pasos 2º y 3º.

Test:
=

Para correr los tests:

    docker exec -it fastapi pytest

Si quieres correr los test por separado de cada colección, por ejemplo:

    docker exec -it fastapi pytest -m users

    docker exec -it fastapi pytest -m libraries

Frontend:
=

Aún está en desarrollo
