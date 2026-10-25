from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from models.ingredient import Ingredient


async def get_ingredients(
    session: AsyncSession,
    name: str | None = None,
) -> list[Ingredient]:
    query = select(Ingredient)
    if name:
        query = query.where(Ingredient.name.ilike(f'{name}%'))
    result = await session.execute(query)
    return list(result.scalars().all())


async def get_ingredient_by_id(
    ingredient_id: int,
    session: AsyncSession,
) -> Ingredient | None:
    query = select(Ingredient).where(Ingredient.id == ingredient_id)
    result = await session.execute(query)
    return result.scalar_one_or_none()
