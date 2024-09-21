from dataclasses import dataclass

from domain.entities.comments import Comment
from infrastructure.db.redis.models import Comment as RedisComment
from infrastructure.repositories.base.redis import BaseRedisRepository


@dataclass
class RedisCommentsRepository(BaseRedisRepository):
    model = Comment

    async def get_by_task_id(self, task: str) -> list[Comment]:
        key = f"tasks:{task}:comments:*"
        return await self.client.get_bulk_json(key)

    async def create_or_update(self, comment: Comment) -> Comment:
        key = f"tasks:{comment.task}:comments:{comment.id}"
        redis_model = RedisComment(**comment.model_dump())
        await self.client.set_json(key, redis_model.model_dump())
        return comment

    async def delete(self, task: str, comment_id: str) -> None:
        key = f"tasks:{task}:comments:{comment_id}"
        await self.client.delete(key)
