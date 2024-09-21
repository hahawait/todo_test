from abc import ABC
from dataclasses import dataclass

from infrastructure.db.redis.client import RedisClient


@dataclass
class BaseRedisRepository(ABC):
    model = None
    client: RedisClient
