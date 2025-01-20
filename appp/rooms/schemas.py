from pydantic import BaseModel
from typing import Optional


class RoomCreateSchema(BaseModel):
    hotel_id: int
    name: str
    description: str
    price: float
    services: list
    quantity: int
    image_id: int

class RoomResponseSchema(RoomCreateSchema):
    id: int

    class Config:
        from_attributes = True


class RoomUpdateImageSchema(BaseModel):
    image_id: int

