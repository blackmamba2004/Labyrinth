from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase

from backend.config.settings import settings
from backend.internal.models.mixins import ModelMixin

DATABASE_URL = settings.get_db_url()

engine = create_async_engine(DATABASE_URL, echo=True)

async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase, ModelMixin):
    pass