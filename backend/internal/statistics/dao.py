from sqlalchemy import select, func

from backend.config.database import async_session_maker
from backend.internal.models.dao import BaseDAO
from backend.internal.statistics.models import Statistic


class StatisticDAO(BaseDAO):
    model = Statistic

    @classmethod
    async def get_average_duration(cls, user_id: int, last_count: int):
        async with async_session_maker() as session:
            subquery = (
                select(cls.model.duration)
                .where(cls.model.user_id == user_id)
                .order_by(cls.model.id.desc())
                .limit(last_count)
            )

            query = select(func.avg(subquery.c.duration))
            result = await session.execute(query)
            average_duration = result.scalar()
            return average_duration
