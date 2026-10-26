from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from models.user import User

from schemas.user import UserCreate

from core.security import hash_password


async def get_user_by_id(user_id: int, session: AsyncSession) -> User | None:
    query = select(User).where(User.id == user_id)
    result = await session.execute(query)
    return result.scalar_one_or_none()


async def get_user_by_email(user_email: str, session: AsyncSession) -> User | None:
    query = select(User).where(User.email == user_email)
    result = await session.execute(query)
    return result.scalar_one_or_none()


async def get_user_by_username(user_username: str, session: AsyncSession) -> User | None:
    query = select(User).where(User.username == user_username)
    result = await session.execute(query)
    return result.scalar_one_or_none()
    

async def create_user(user_in: UserCreate, session: AsyncSession) -> User:
    user_data = user_in.model_dump()
    raw_password = user_data.pop('password')
    hashed_password = hash_password(raw_password)

    db_user = User(**user_data, hashed_password=hashed_password)

    session.add(db_user)
    await session.commit()
    await session.refresh(db_user)
    
    return db_user
