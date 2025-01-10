from fastapi import FastAPI, Query
from typing import Optional
from datetime import date
from pydantic import BaseModel


app = FastAPI(
    title="FastAPI PetProject Bookings Hotel",
    version="0.1",
    description="This is a very fancy project, with auto docs for the API and everything",
)

@app.get("/helloWorld")
def read_root():
    return {"Hello": "World"}


@app.get("/hotel/{hotel_id}")#path parameter
def read_hotel(hotel_id: int):
    return {"hotel_id": hotel_id,
            "hotel_name": "Bridge Hotel",
            }

@app.get("/hotel/{hotel_id}/room/{room_id}")#path parameter #example: /hotel/1/room/2
def read_room(hotel_id: int, room_id: int, date_from: str, date_to: str, room_name: str):
    return {"hotel_id": hotel_id,#path parameter
            "room_id": room_id,#path parameter
            "date_from": date_from,#query parameter #example: date_from=today
            "date_to": date_to,#query parameter #example: date_to=tomorrow
            "room_name": room_name#query parameter #example: room_name=Suite
            } #http://127.0.0.1:8000/hotel/1/room/2?date_from=today&date_to=tomorrow&room_name=Deluxe


@app.get("/hotel")
def get_hotels(
    location: str,
    date_from: date,
    date_to: date,
    has_spa: Optional[bool] = None,
    stars: Optional[int] = Query(None, ge=1, le=5),
):
    return date_from, date_to


class SBooking(BaseModel):
    room_id: int
    date_from: date
    date_to: date




@app.post("/bookings")
def add_booking(booking: SBooking):
    return booking




class SHotel(BaseModel):
    adress: str
    name: str
    stars: int
    #has_spa: bool #not used in this example, validation error


@app.get("/hotelss", response_model=list[SHotel])
def get_hotel(
    location: str,
    date_from: str,
    date_to: str,
    has_spa: Optional[bool] = None,
    stars: Optional[int] = Query(None, ge=1, le=5),
) : #-> list[SHotel]:
    hotels = [
        {"name": "Bridge Hotel", "adress": "London", "stars": 5},
        {"name": "Hotel California", "adress": "California", "stars": 4},
        {"name": "Hotel Moscow", "adress": "Moscow", "stars": 3},
        {"name": "Hotel Paris", "adress": "Paris", "stars": 2},
        {"name": "Hotel Berlin", "adress": "Berlin", "stars": 1},
        {"name": "Hotel Rome", "adress": "Rome", "stars": 5},
        {"name": "Hotel Madrid", "adress": "Madrid", "stars": 4},
    ]
    return hotels
    

    

