from redis.asyncio import Redis


class RedisClient:
    """
    Базовый класс модели, предоставляющий методы для работы с данными redis.
    """

    def __init__(
            self,
            connection: Redis,
    ) -> None:
        self._connection = connection

    async def set_json(self, key: str, value: dict):
        await self._connection.json().set(key, ".", value)

    async def delete(self, key: str):
        await self._connection.json().delete(key, ".")

    async def get_bulk_json(self, key_pattern: str) -> list[dict]:
        keys = await self._connection.keys(key_pattern)
        if not keys:
            return []
        return await self._connection.json().mget(keys=keys, path=".")
