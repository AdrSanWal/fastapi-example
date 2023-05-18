import os

from fastapi import Request


def get_collection_from_url(request: Request):
    collection = str(request.url).split('/')
    return collection[-2]


def get_collections_names():
    dir_path = '/code/db/filldb'
    files = filter(lambda x: x.split('.')[1] == 'json', os.listdir(dir_path))
    json_files = filter(lambda x: x.split('.')[1] == 'json', files)

    filenames = [_.split('.')[0] for _ in json_files]

    return [filename for filename in filenames]
