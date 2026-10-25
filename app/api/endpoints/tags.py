from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.db import get_async_session
from crud import tag as tag_crud

from schemas.tag import TagResponse

router = APIRouter()


@router.get('/', response_model=list[TagResponse])
async def get_tags(
    session: AsyncSession = Depends(get_async_session),
):
    return await tag_crud.get_tag(session)


@router.get('/{tag_id}/', response_model=TagResponse)
async def get_tag(
    tag_id: int,
    session: AsyncSession = Depends(get_async_session)
):
    tag = await tag_crud.get_tag_by_id(tag_id, session)
    if not tag:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Тег не найден'
        )
    return tag