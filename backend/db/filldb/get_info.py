from asyncio import run as runasyncio
from json import load
import os

from fastapi import HTTPException

from db.models import Location, Address, Organization, Model
from api.crud import post_instance


async def add_to_db(model: Model, collection: str):
    return await post_instance(collection, model)


dir_path = os.path.dirname(os.path.realpath(__file__))
files = filter(lambda x: x.split('.')[1] == 'json', os.listdir(dir_path))
json_files = filter(lambda x: x.split('.')[1] == 'json', files)

filenames = [_.split('.')[0] for _ in json_files]

for filename in filenames:

    with open(f'db/filldb/{filename}.json', 'r') as file:
        data = load(file)
        new_elements = 0
        print(f'Leyendo {filename}')

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
                    'schedule': element.get('organization', None).get('schedule', None),
                    'services': element.get('organization', None).get('services', None)
                }

                organization = Organization(**organization)

                model = {
                    'model': filename,
                    'title': element['title'],
                    'relation': element['relation'],
                    'address': address,
                    'location': location,
                    'organization': organization
                }

                model = Model(**model)

                print(f'Elementos comprobados: {i}', end="\r")

                try:
                    runasyncio(add_to_db(model, filename))
                    new_elements += 1
                except HTTPException:
                    pass

            except KeyError:
                continue

        print(f'\nNuevas instancias en la colección {filename}: {new_elements}', end="\n\n")

        # add route to new collection

        main_file = 'api/main.py'

        with open(main_file, 'r+') as mainfile:
            data = mainfile.read()
            if filename not in data:
                mainfile.write(f"app.include_router(tables.router, prefix='/{filename}',\n"
                               + f"                   tags=['{filename}'])\n")
