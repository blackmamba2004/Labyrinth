from sqlalchemy import insert, select

from backend.config.database import async_session_maker, Base


class BaseDAO:
    model: Base = None

    @classmethod
    async def create(cls, **data):
        async with async_session_maker() as session:
            query = (
                insert(cls.model)
                .values(**data)
                .returning(cls.model)
            )
            result = await session.execute(query)
            await session.commit()
            return result.scalar_one_or_none()

    @classmethod
    async def filter(cls, **filter_by):
        async with async_session_maker() as session:
            query = select(cls.model).filter_by(**filter_by)
            result = await session.execute(query)
            return result.scalar_one_or_none()
