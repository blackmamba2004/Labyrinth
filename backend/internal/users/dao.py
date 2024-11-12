from backend.internal.models.dao import BaseDAO
from backend.internal.users.models import User


class UserDAO(BaseDAO):
    model = User
