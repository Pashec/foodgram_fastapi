from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.tag import Tag


async def get_tag(session: AsyncSession) -> list[Tag]:

    query = select(Tag)

    result = await session.execute(query)

    return list(result.scalars().all())


async def get_tag_by_id(
    tag_id: int,
    session: AsyncSession
) -> Tag | None:

    query = select(Tag).where(Tag.id ==tag_id)
    result = await session.execute(query)
    return result.scalar_one_or_none()


