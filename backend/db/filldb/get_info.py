import json

from ..models import Coord, Address, Organization, Model

file_name = 'aparcamientos publicos'

with open(f'data/{file_name}.json', 'r') as file:
    data = json.load(file)

    for element in data['@graph']:
        coord = Coord()
        address = Address()
        organization = Organization()
        model = Model()

        model.model = file_name
        model.title = element['title']
        model.relation = element['relation']

        print(model)
