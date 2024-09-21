from datetime import datetime

from pydantic import BaseModel, field_serializer


class Comment(BaseModel):
    id: str
    task: str
    user: int
    content: str
    created_at: datetime
    updated_at: datetime

    @field_serializer('created_at', 'updated_at')
    def serialize_datetime(self, value: datetime) -> str:
        return value.timestamp()
