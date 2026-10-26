from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_async_session
from crud import user as crud_user
from schemas.user import UserCreate, UserResponse

router = APIRouter()


@router.post(
    '/',
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_user(
    user_in: UserCreate,
    session: AsyncSession = Depends(get_async_session)
) -> UserResponse:
    if await crud_user.get_user_by_email(user_in.email, session):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Пользователь с таким email уже зарегистрирован.'
        )
    if await crud_user.get_user_by_username(user_in.username, session):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Пользователь с таким именем уже зарегистрирован.'
        )
    new_user = await crud_user.create_user(user_in, session)
    return new_user