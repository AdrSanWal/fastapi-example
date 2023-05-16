# FastAPI-example

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

    docker exec fastapi python3 backend/db/filldb/get_info.py

Documentación:
=

    http://localhost:8000/docs

    http://localhost:8000/redoc

Datos:
=

Ahora mismo los servicios almacenados son:

<ul>
  <li>Cementerios</li>
  <li>Centros de enseñanza</li>
  <li>Parques de bomberos</li>
  <li>Librerías</li>
  <li>Monumentos</li>
  <li>Piscinas municipales</li>
  <li>Museos</li>
  <li>Parques</li>
  <li>Comisarías</li>
  <li>Parkings públicos</li>
  <li>Colegios públicos</li>
  <li>Puntos limpios</li>
  <li>Polideportivos</li>
</ul>

  Si quieres incorporar más sevicios a la base de datos, descarga el json
  correspondiente de la <a href='https://datos.madrid.es/portal/site/egob/menuitem.214413fe61bdd68a53318ba0a8a409a0/?vgnextoid=b07e0f7c5ff9e510VgnVCM1000008a4a900aRCRD&vgnextchannel=b07e0f7c5ff9e510VgnVCM1000008a4a900aRCRD&vgnextfmt=default'>API de datos abiertos de la comunidad de madrid</a>.

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
