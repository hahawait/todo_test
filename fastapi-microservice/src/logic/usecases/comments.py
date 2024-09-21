from dataclasses import dataclass

from domain.entities.comments import Comment
from infrastructure.repositories.comments.redis import RedisCommentsRepository
from infrastructure.clients.api.comments import CommentsClient
from logic.usecases.base import BaseUseCase


@dataclass
class GetCommentsUseCase(BaseUseCase):
    repo: RedisCommentsRepository
    cli: CommentsClient

    async def execute(self, task_id: str, user_id: int, token: str) -> list[Comment]:
        comments = await self.repo.get_by_task_id(task_id)
        if not comments:
            async with self.cli as cli:
                comments = await cli.get_comments(task_id=task_id, user_id=user_id, token=token)
            for comment in comments:
                await self.repo.create_or_update(Comment(**comment))
        return comments


@dataclass
class CreateCommentUseCase(BaseUseCase):
    repo: RedisCommentsRepository
    cli: CommentsClient

    async def execute(self, task_id: str, user_id: int, content: str, token: str) -> Comment:
        async with self.cli as cli:
            comment_data = await cli.create_comment(task_id=task_id, user_id=user_id, content=content, token=token)
        comment = Comment(**comment_data)
        await self.repo.create_or_update(comment)
        return comment


@dataclass
class UpdateCommentUseCase(BaseUseCase):
    repo: RedisCommentsRepository
    cli: CommentsClient

    async def execute(self, comment_id: str, content: str, token: str) -> Comment:
        async with self.cli as cli:
            comment_data = await cli.update_comment(comment_id=comment_id, content=content, token=token)
        comment = Comment(**comment_data)
        await self.repo.create_or_update(comment)
        return comment


@dataclass
class DeleteCommentUseCase(BaseUseCase):
    repo: RedisCommentsRepository
    cli: CommentsClient

    async def execute(self, task_id: str, comment_id: str, token: str) -> None:
        async with self.cli as cli:
            await cli.delete_comment(comment_id=comment_id, token=token)
        await self.repo.delete(task_id=task_id, comment_id=comment_id)
