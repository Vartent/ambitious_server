import os.path

from pydantic import BaseSettings


class Settings(BaseSettings):
    server_host: str = '127.0.0.1'
    server_port: int = '8001'
    database_url: str = 'sqlite:///.database.sqlite3'

    jwt_secret: str
    jwt_algorithm: str = 'HS256'
    jwt_expiration: int = 3600


settings = Settings(
    _env_file=os.path.expanduser('/Users/someone/PycharmProjects/fast-api-tutorial-project/src/workshop/.env'),
    _env_file_encoding='utf-8'
)