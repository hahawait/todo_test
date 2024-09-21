from dishka import Provider, Scope, provide

from infrastructure.repositories.comments.redis import RedisCommentsRepository
from infrastructure.clients.api.comments import CommentsClient
from logic.usecases.comments import GetCommentsUseCase, CreateCommentUseCase, UpdateCommentUseCase, DeleteCommentUseCase


class CommentsProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def get_comments_usecase(self, repo: RedisCommentsRepository, cli: CommentsClient) -> GetCommentsUseCase:
        return GetCommentsUseCase(repo=repo, cli=cli)

    @provide
    def create_comment_usecase(self, repo: RedisCommentsRepository, cli: CommentsClient) -> CreateCommentUseCase:
        return CreateCommentUseCase(repo=repo, cli=cli)

    @provide
    def update_comment_usecase(self, repo: RedisCommentsRepository, cli: CommentsClient) -> UpdateCommentUseCase:
        return UpdateCommentUseCase(repo=repo, cli=cli)

    @provide
    def delete_comment_usecase(self, repo: RedisCommentsRepository, cli: CommentsClient) -> DeleteCommentUseCase:
        return DeleteCommentUseCase(repo=repo, cli=cli)
