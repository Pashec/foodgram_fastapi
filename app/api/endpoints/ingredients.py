from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_async_session
from crud import ingredient as ingredient_crud
from schemas.ingredient import IngredientResponse

router = APIRouter()


@router.get('/', response_model=list[IngredientResponse])
async def get_ingredients(
    name: str | None = None,
    session: AsyncSession = Depends(get_async_session),
):
    return await ingredient_crud.get_ingredients(session, name=name)


@router.get('/{ingredient_id}/', response_model=IngredientResponse)
async def get_ingredient(
    ingredient_id: int,
    session: AsyncSession = Depends(get_async_session),
):
    ingredient = await ingredient_crud.get_ingredient_by_id(ingredient_id, session)
    if not ingredient:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Ингредиент не найден',
        )
    return ingredient
