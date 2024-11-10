from fastapi import APIRouter, Security

from backend.internal.levels.service import generate_maze
from backend.pkg.auth.middlewares.jwt.service import check_access_token


router = APIRouter(prefix='/levels', tags=['Levels'])


@router.get('/level', dependencies=[Security(check_access_token)])
async def get_level(row_count: int = 27, column_count: int = 27) -> list[list[int]]:
    return generate_maze(row_count, column_count)
