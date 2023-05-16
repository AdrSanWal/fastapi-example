import os
from pydantic import BaseSettings

from dotenv import load_dotenv
from fastapi.testclient import TestClient


load_dotenv()


class Settings():
    def __init__(self):
        self.hostname = os.getenv('MONGO_HOSTNAME')
        self.port = os.getenv('MONGO_PORT')
        self.username = os.getenv('MONGO_USER')
        self.password = os.getenv('MONGO_PASS')
        self.db = os.getenv('MONGO_DB')


class AuthSettings():
    def __init__(self):
        self.secret = os.getenv('AUTH_SECRET')
        self.algorithm = os.getenv('AUTH_ALGORITHM')


STATIC_FOLDER_IMAGES = 'backend/static/images'


settings = Settings()
auth_settings = AuthSettings()
