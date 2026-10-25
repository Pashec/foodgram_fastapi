from pydantic import BaseModel, ConfigDict, Field


class TagBase(BaseModel):
    name: str = Field(..., max_length=32)
    slug: str = Field(..., max_length=32)


class TagResponse(TagBase):
    id: int

    model_config = ConfigDict(from_attributes=True)