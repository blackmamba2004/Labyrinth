import asyncio
from sqlalchemy import select

from backend.config.database import async_session_maker
from backend.internal.users.models import User
from backend.internal.users.schemas import UserOut


async def main():
    async with async_session_maker() as session:
        query = select(User).where(User.id == 1)
        result = await session.execute(query)
        result = result.scalar_one_or_none()
        print(result)
        print(UserOut.model_validate(result))

asyncio.run(main())