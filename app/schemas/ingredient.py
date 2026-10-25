from pydantic import BaseModel, ConfigDict, Field


class IngredientBase(BaseModel):
    name: str = Field(..., max_length=128)
    measurement_unit: str = Field(..., max_length=64)


class IngredientResponse(IngredientBase):
    id: int

    model_config = ConfigDict(from_attributes=True)