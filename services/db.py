from ctypes import cast
from sqlalchemy import create_engine, URL
from singleton_decorator import singleton
from services.config import Config

from sqlalchemy.dialects import postgresql


@singleton
class DB:
    def __init__(self) -> None:
        connection_string: URL = self.generate_connection_string(
            Config().get('database'))
        self.engine = create_engine(connection_string)

    def generate_connection_string(self, config) -> URL:
        match config['driver']:
            case 'postgresql':
                return URL.create(
                    "postgresql",
                    username=config["username"],
                    password=config["password"],  # plain (unescaped) text
                    host=config["host"],
                    port=config["port"],
                    database=config["database"]
                )


