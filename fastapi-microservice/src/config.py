import hashlib
from dataclasses import dataclass
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class BaseConfig(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


class BotConfig(BaseConfig):
    TOKEN: str

    @property
    def HASHED_TOKEN(self):
        return hashlib.sha256(self.TOKEN.encode()).hexdigest()


class AppConfig(BaseConfig):
    MODE: Literal["DEV", "TEST", "PROD", "LOCAL"]
    LOG_LEVEL: Literal["DEBUG", "INFO", "WARN", "ERROR", "FATAL"]
    TITLE: str
    DESCRIPTION: str
    VERSION: str
    SENTRY_DSN: str | None = None
    ADMIN_USERNAME: str
    ADMIN_PASSWORD: str

    @property
    def is_production(self):
        return self.MODE == "PROD"

    @property
    def is_dev(self):
        return self.MODE == "DEV"

    @property
    def is_local(self):
        return self.MODE == "LOCAL"


class RedisConfig(BaseSettings):
    REDIS_HOST: str = 'localhost'
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: str = 'foobared'

    @property
    def redis_url(self):
        return f"redis://:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}/0"


class AuthSetting(BaseConfig):
    ALGORITHM: str
    PUBLIC_KEY: str


class DjangoConfig(BaseConfig):
    BASE_URL: str
    COMMENTS_ENDPOINT: str


@dataclass
class Config:
    app: AppConfig
    bot: BotConfig
    redis_config: RedisConfig
    auth_config: AuthSetting
    django: DjangoConfig


def get_config():
    return Config(
        app=AppConfig(),
        bot=BotConfig(),
        redis_config=RedisConfig(),
        auth_config=AuthSetting(),
        django=DjangoConfig(),
    )
