from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Date, Computed
from datetime import datetime
from app.hotels.models import Hotels
from app.rooms.models import Rooms
from app.users.models import Users


class Bookings(Base):
    __tablename__ = "bookings"

    id         : Mapped[int] = mapped_column(primary_key=True, nullable=False)
    room_id    : Mapped[int] = mapped_column(ForeignKey("rooms.id"), nullable=False)
    user_id    : Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    date_from  : Mapped[datetime] = mapped_column(Date, nullable=False)
    date_to    : Mapped[datetime] = mapped_column(Date, nullable=False)
    price      : Mapped[int] = mapped_column(nullable=False)
    total_cost : Mapped[int] = mapped_column(Computed("(date_to - date_from) * price"))
    totel_days : Mapped[int] = mapped_column(Computed("date_to - date_from"))
    
    hotelB      : Mapped[list["Hotels"]] = relationship(
        back_populates="bookings"
    )

    def __repr__(self):
        return f"<Booking #{self.id}>"