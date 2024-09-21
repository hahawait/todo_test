from pydantic import BaseModel, Field, EmailStr


class ErrorSchema(BaseModel):
    detail: str


class UserSchema(BaseModel):
    id: int = Field(None, validation_alias="user_id")
    email: EmailStr | None = None
    name: str | None = None
    token: str | None = None
