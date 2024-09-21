from typing import Annotated

from dishka.integrations.fastapi import inject, FromDishka
from fastapi import APIRouter, Depends

from app.api.dependencies import get_user
from app.api.comments.schemas import CommentResponseDTO, CommentCreateDTO, CommentUpdateDTO, CommentDeleteDTO
from app.api.schemas import ErrorSchema, UserSchema
from logic.usecases.comments import GetCommentsUseCase, CreateCommentUseCase, UpdateCommentUseCase, DeleteCommentUseCase

router = APIRouter(
    prefix="/comments",
    tags=["comments"],
    responses={
        401: {"description": "Unauthorized", "model": ErrorSchema},
    }
)


@router.get("/{task_id}")
@inject
async def get_comments_by_task_id(
    task_id: str,
    user_id: int,
    use_case: FromDishka[GetCommentsUseCase],
    user: Annotated[UserSchema, Depends(get_user())]
) -> list[CommentResponseDTO]:
    """
    Получение комментариев по id задачи
    """
    return await use_case.execute(
        task_id=task_id,
        user_id=user_id,
        token=user.token
    )


@router.post("")
@inject
async def create_comment(
    use_case: FromDishka[CreateCommentUseCase],
    user: Annotated[UserSchema, Depends(get_user())],
    create_dto: CommentCreateDTO
) -> CommentResponseDTO:
    return await use_case.execute(
        task_id=create_dto.task,
        user_id=create_dto.user,
        content=create_dto.content,
        token=user.token
    )


@router.put("")
@inject
async def update_comment(
    use_case: FromDishka[UpdateCommentUseCase],
    user: Annotated[UserSchema, Depends(get_user())],
    update_dto: CommentUpdateDTO
) -> CommentResponseDTO:
    return await use_case.execute(
        comment_id=update_dto.comment_id,
        content=update_dto.content,
        token=user.token
    )


@router.delete("")
@inject
async def delete_comment(
    use_case: FromDishka[DeleteCommentUseCase],
    user: Annotated[UserSchema, Depends(get_user())],
    delete_dto: CommentDeleteDTO
) -> CommentResponseDTO:
    return await use_case.execute(
        task_id=delete_dto.task_id,
        comment_id=delete_dto.comment_id,
        token=user.token
    )
