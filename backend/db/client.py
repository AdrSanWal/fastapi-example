from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError, OperationFailure

from fastapi import APIRouter

from api.settings import settings

router = APIRouter()


class ConnectionMongoDB:

    def mongoclient(self):
        params = {
            'host': f'{settings.hostname}:{settings.port}',
            'username': settings.username,
            'password': settings.password
        }

        try:
            return MongoClient(**params)
        except OperationFailure:
            return ("Database not found.")
        except ServerSelectionTimeoutError:
            return ("MongoDB Server is down.")

client = ConnectionMongoDB().mongoclient()
