from appp.users.models import Users
from appp.database import async_session_maker
from sqlalchemy import select
from appp.dao.basedao import BaseDAO


class UserDAO(BaseDAO):
    model = Users
    