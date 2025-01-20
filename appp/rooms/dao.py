from app.rooms.models import Rooms
from app.dao.basedao import BaseDAO


class RoomDAO(BaseDAO):
    model = Rooms
    