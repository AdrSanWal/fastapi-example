from asyncio import run as runasyncio
from json import load
import os

from fastapi import HTTPException

from db.models import Location, Address, Organization, Model
from api.crud import post_instance


file_name = 'aparcamientos publicos'


dir_path = os.path.dirname(os.path.realpath(__file__))
files = filter(lambda x: x.split('.')[1] == 'json', os.listdir(dir_path))
json_files = filter(lambda x: x.split('.')[1] == 'json', files)


async def add_to_db(model: Model, collection: str):
    return await post_instance(collection, model)

for json_file in json_files:
    file = json_file.split('.')[0]

    with open(f'backend/db/filldb/{file}.json', 'r') as file:
        data = load(file)
        new_elements = 0
        print(f'Leyendo {json_file}')

        for i, element in enumerate(data['@graph']):

            try:
                address = {
                    'locality': element['address']['locality'],
                    'postal_code': element['address']['postal-code'],
                    'street': element['address']['street-address']
                }

                address = Address(**address)

                location = {
                    'lat': element['location']['latitude'],
                    'lng': element['location']['longitude']
                }

                location = Location(**location)

                organization = {
                    'name': element['organization']['organization-name'],
                    'description': element['organization']['organization-desc'],
                    'schedule': element['organization']['schedule'],
                    'services': element['organization']['services']
                }

                organization = Organization(**organization)

                model = {
                    'model': json_file,
                    'title': element['title'],
                    'relation': element['relation'],
                    'address': address,
                    'location': location,
                    'organization': organization
                }

                model = Model(**model)

                print(f'Elementos comprobados: {i}', end="\r")

                try:
                    runasyncio(add_to_db(model, json_file))
                    new_elements += 1
                except HTTPException:
                    pass

            except KeyError:
                continue

        print(f'\nNuevas instancias en la colección {json_file}: {new_elements}', end="\n\n")



# with open(f'backend/db/filldb/{file_name}.json', 'r') as file:
#     data = load(file)
#     new_elements = 0

#     for i, element in enumerate(data['@graph']):

#         address = {
#             'locality': element['address']['locality'],
#             'postal_code': element['address']['postal-code'],
#             'street': element['address']['street-address']
#         }

#         address = Address(**address)

#         location = {
#             'lat': element['location']['latitude'],
#             'lng': element['location']['longitude']
#         }

#         location = Location(**location)

#         organization = {
#             'name': element['organization']['organization-name'],
#             'description': element['organization']['organization-desc'],
#             'schedule': element['organization']['schedule'],
#             'services': element['organization']['services']
#         }

#         organization = Organization(**organization)

#         model = {
#             'model': file_name,
#             'title': element['title'],
#             'relation': element['relation'],
#             'address': address,
#             'location': location,
#             'organization': organization
#         }

#         model = Model(**model)

#         print(f'Elementos comprobados: {i}', end="\r")

#         try:
#             runasyncio(add_to_db(model))
#             new_elements += 1
#         except HTTPException:
#             pass

#     print(f'\n\nNuevas instancias en la colección {file_name}: {new_elements}.')
