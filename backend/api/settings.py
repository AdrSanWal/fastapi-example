import os
from pydantic import BaseSettings

from dotenv import load_dotenv
from fastapi.testclient import TestClient


load_dotenv()


class Settings(BaseSettings):
    _hostname = os.getenv('MONGO_HOSTNAME')
    _port = os.getenv('MONGO_PORT')
    _username = os.getenv('MONGO_USER')
    _password = os.getenv('MONGO_PASS')
    _db = os.getenv('MONGO_DB')
