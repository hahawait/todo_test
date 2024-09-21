from pydantic import BaseModel


class CommentDeleteDTO(BaseModel):
    task: str
    comment_id: str


class CommentUpdateDTO(BaseModel):
    comment_id: str
    content: str


class CommentCreateDTO(BaseModel):
    task: str
    user: int
    content: str


class CommentResponseDTO(BaseModel):
    id: str
    task: str
    user: int
    content: str
