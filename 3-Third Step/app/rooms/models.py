from app.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import JSON, ForeignKey


class Rooms(Base):
    __tablename__ = "rooms"

    id : Mapped[int] = mapped_column(primary_key=True)
    hotel_id : Mapped[int] = mapped_column(ForeignKey("hotels.id"), nullable=False)
    name : Mapped[str] = mapped_column(nullable=False)
    description : Mapped[str] = mapped_column(nullable=False)
    price : Mapped[float] = mapped_column(nullable=False)
    services : Mapped[JSON] = mapped_column(type_=JSON, nullable=False)
    quantity : Mapped[int] = mapped_column(nullable=False)
    image_id : Mapped[int]

    hotel = relationship("Hotels", back_populates="rooms")
    bookings = relationship("Bookings", back_populates="room")

