from app.bookings.models import Bookings
from app.database import async_session_maker
from sqlalchemy import select
from app.dao.basedao import BaseDAO


class BookingDAO(BaseDAO):
    model = Bookings
    