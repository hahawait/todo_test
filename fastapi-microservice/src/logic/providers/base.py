from dishka import Provider, Scope, provide

from config import Config, get_config
from infrastructure.clients.api.comments import CommentsClient
from infrastructure.db.redis.connection import RedisConnection
from infrastructure.db.redis.client import RedisClient
from infrastructure.repositories.comments.redis import RedisCommentsRepository


class BaseProvider(Provider):
    @provide(scope=Scope.APP)
    def config(self) -> Config:
        return get_config()

    @provide(scope=Scope.APP)
    def redis_connection(self, config: Config) -> RedisConnection:
        return RedisConnection(
            # url=config.redis_config.redis_url,
            host=config.redis_config.REDIS_HOST,
            port=config.redis_config.REDIS_PORT,
        ).get_client()

    @provide(scope=Scope.APP)
    def redis_client(self, connection: RedisConnection) -> RedisClient:
        return RedisClient(connection)

    @provide(scope=Scope.APP)
    def comments_repository(self, client: RedisClient) -> RedisCommentsRepository:
        return RedisCommentsRepository(client)

    @provide(scope=Scope.APP)
    def comments_client(self, config: Config) -> CommentsClient:
        return CommentsClient(base_url=config.django.BASE_URL, comments_endpoint=config.django.COMMENTS_ENDPOINT)
