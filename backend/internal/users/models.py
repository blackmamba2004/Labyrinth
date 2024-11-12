from sqlalchemy.orm import relationship

from backend.internal.users.base import BaseUser
from backend.internal.statistics.models import Statistic


class User(BaseUser):
    statistics = relationship('Statistic', back_populates='user')
