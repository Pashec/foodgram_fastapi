from fastapi import APIRouter


router = APIRouter()

@router.get('/ping')
async def check_health():
    return {'status': 'ok'}