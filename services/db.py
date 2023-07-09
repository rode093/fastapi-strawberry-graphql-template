from sqlalchemy import create_engine, URL
from singleton_decorator import singleton
@singleton
class DB:
    def __init__(self, config) -> None:
        self.engine = create_engine(self.generate_connection_string(config))
        
    def generate_connection_string(self, config)-> URL:
        match config.postgresql:
            case 'postgresql':
                return URL.create(
                        "postgresql+pg8000",
                        username=config["username"],
                        password=config["password"],  # plain (unescaped) text
                        host=config["host"],
                        port=config["port"],
                        database=config["database"]
                    )