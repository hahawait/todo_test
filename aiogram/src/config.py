import hashlib
from dataclasses import dataclass

from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class BotConfig(BaseConfig):
    TOKEN: str

    @property
    def HASHED_TOKEN(self):
        return hashlib.sha256(self.TOKEN.encode()).hexdigest()


class FastApiConfig(BaseConfig):
    FASTAPI_BASE_URL: str
    COMMENT_URL: str = '/comments'


class DjangoConfig(BaseConfig):
    DJANGO_BASE_URL: str
    TASK_URL: str = '/api/tasks'


@dataclass
class Config:
    bot: BotConfig
    fastapi: FastApiConfig
    django: DjangoConfig


def get_config():
    return Config(
        bot=BotConfig(),
        fastapi=FastApiConfig(),
        django=DjangoConfig(),
    )
