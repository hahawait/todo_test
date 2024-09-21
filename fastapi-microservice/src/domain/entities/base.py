from abc import ABC
from datetime import datetime, timezone

from pydantic import BaseModel, Field


class BaseEntity(ABC, BaseModel):
    created_at: datetime = Field(default_factory=lambda: datetime.now(tz=timezone.utc))
    updated_at: datetime | None = None

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other: "BaseEntity"):
        return self.id == other.id
