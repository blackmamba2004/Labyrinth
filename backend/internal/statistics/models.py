from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.config.database import Base
from backend.internal.models.fields import int_pk


class Statistic(Base):
    id: Mapped[int_pk]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id', ondelete='Cascade'))
    row_count: Mapped[int]
    column_count: Mapped[int]
    duration: Mapped[int]

    user = relationship('User', back_populates='statistics')
