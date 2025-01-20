from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import JSON
from appp.database import Base
from appp.rooms.models import Rooms
from appp.bookings.models import Bookings


class Hotels(Base):
    __tablename__ = "hotels"

    id             : Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name           : Mapped[str] = mapped_column(nullable=False)
    location       : Mapped[str] = mapped_column(nullable=False)
    services       : Mapped[list[str]] = mapped_column(JSON)
    rooms_quantity : Mapped[int] = mapped_column(nullable=False)
    image_id       : Mapped[int]
    
    rooms          : Mapped[list["Rooms"]] = relationship(
        back_populates="hotelR"
    )
    bookings       : Mapped[list["Bookings"]] = relationship(
        back_populates="hotelB"
    )
    