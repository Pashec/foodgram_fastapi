from enum import unique
from pydantic import BaseModel, ConfigDict, EmailStr, Field


class UserBase(BaseModel):
    email: EmailStr
    username: str = Field(..., max_length=128)
    first_name: str = Field(..., max_length=128)
    last_name: str = Field(..., max_length=128)


class UserCreate(UserBase):
    password: str = Field(min_length=6, max_length=128)


class UserResponse(UserBase):
    id: int
    avatar: str | None = None

    model_config = ConfigDict(from_attributes=True)