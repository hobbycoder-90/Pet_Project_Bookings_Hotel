from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import JSON
from app.database import Base


class Hotels(Base):
    __tablename__ = "hotels"

    id : Mapped[int] = mapped_column(primary_key=True)
    name : Mapped[str] = mapped_column(nullable=False)
    location : Mapped[str] = mapped_column(nullable=False)
    services : Mapped[JSON] = mapped_column(type_=JSON, nullable=True)
    rooms_quantity : Mapped[int] = mapped_column(nullable=False)
    image_id : Mapped[int]

    rooms = relationship("Rooms", back_populates="hotel")
    bookings = relationship("Bookings", back_populates="hotel")
