import os
from pydantic import BaseSettings

from dotenv import load_dotenv
from fastapi.testclient import TestClient


load_dotenv()


class Settings():
    def __init__(self):
        self._hostname = os.getenv('MONGO_HOSTNAME')
        self._port = os.getenv('MONGO_PORT')
        self._username = os.getenv('MONGO_USER')
        self._password = os.getenv('MONGO_PASS')
        self._db = os.getenv('MONGO_DB')


class AuthSettings():
    def __init__(self):
        self._secret = os.getenv('AUTH_SECRET')
        self._algorithm = os.getenv('AUTH_ALGORITHM')


settings = Settings()
auth_settings = AuthSettings()
