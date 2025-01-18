from app.hotels.models import Hotels
from app.database import async_session_maker
from sqlalchemy import select
from app.dao.basedao import BaseDAO


class HotelDAO(BaseDAO):
    model = Hotels
    