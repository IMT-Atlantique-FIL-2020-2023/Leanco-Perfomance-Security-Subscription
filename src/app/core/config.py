import secrets
from typing import Any, Dict, List, Optional, Union

from jose import jwk
from jose.backends.base import Key
from jose.constants import ALGORITHMS
from pydantic import (
    AnyHttpUrl,
    BaseSettings,
    PostgresDsn,
    validator, FilePath,
)


class Settings(BaseSettings):
    API_BASE_URL: str = "/api"
    PROJECT_NAME: str

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200",
    # "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(
            cls, v: Union[str, List[str]]
    ) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    POSTGRES_SERVER: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(
            cls, v: Optional[str], values: Dict[str, Any]
    ) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    # Server CERT
    SERVER_PRIVATE_KEY_PATH: FilePath
    SERVER_PUBLIC_CERT_PATH: FilePath
    SERVER_PRIVATE_KEY: Key = None
    SERVER_PUBLIC_CERT: str = ''

    @validator("SERVER_PRIVATE_KEY")
    def get_server_private_key(cls, v: bool, values: Dict[str, Any]) -> Key:
        file = open(values.get('SERVER_PRIVATE_KEY_PATH'), "r")
        return jwk.construct(file.read(), algorithm=ALGORITHMS.RS384)

    @validator("SERVER_PUBLIC_CERT")
    def get_server_public_cert(cls, v: bool, values: Dict[str, Any]) -> str:
        file = open(values.get('SERVER_PUBLIC_CERT_PATH'), "r")
        return file.read()

    class Config:
        case_sensitive = True
        env_file = ".env"


settings = Settings()
