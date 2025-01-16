from pydantic import BaseModel
from datetime import date


class BookingCreateSchema(BaseModel):
    user_id: int
    room_id: int
    hotel_id: int
    date_from: date
    date_to: date
    price: int




class BookingResponseSchema(BookingCreateSchema):
    id: int
    total_cost: int
    totel_days: int

    class Config:
        from_attributes = True



    
