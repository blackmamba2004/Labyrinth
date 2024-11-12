from fastapi import APIRouter, Security, Request

from backend.pkg.auth.middlewares.jwt.service import check_access_token
from backend.internal.statistics.dao import StatisticDAO
from backend.internal.statistics.schemas import StatisticIn, StatisticOut


router = APIRouter(prefix='/statistics', tags=['Statistics'])


@router.post('', dependencies=[Security(check_access_token)])
async def create_statistic(request: Request, body: StatisticIn) -> StatisticOut:
    return await StatisticDAO.create(
        user_id=request.state.user.id,
        row_count=body.row_count,
        column_count=body.column_count,
        duration=body.duration
    )


@router.get('', dependencies=[Security(check_access_token)])
async def get_statistic(request: Request, last_count: int) -> float:
    return await StatisticDAO.get_average_duration(request.state.user.id, last_count)
