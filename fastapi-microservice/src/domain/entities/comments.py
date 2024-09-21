from pydantic import Field

from domain.entities.base import BaseEntity


class Comment(BaseEntity):
    id: str
    task: str
    user: int
    content: str
