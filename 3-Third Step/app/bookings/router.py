from fastapi import APIRouter, Depends
from app.bookings.models import Bookings
from app.database import async_session_maker
from sqlalchemy import select
from app.exceptions import BookingNotFoundExeption
from app.bookings.schemas import BookingCreateSchema, BookingResponseSchema
from app.bookings.dao import BookingDAO
from app.users.models import Users
from app.auth.dependencies import get_current_user



router = APIRouter(
    prefix="/bookings",
    tags=["Bookings"],
)

@router.get("/", response_model=list[BookingResponseSchema])
async def get_bookings(user: Users = Depends(get_current_user)):
    return await BookingDAO.find_all()

@router.get("/mybookings")
async def get_my_bookings(user: Users = Depends(get_current_user)):
    return await BookingDAO.find_all(user_id=user.id)


@router.get("/{booking_id}", response_model=BookingResponseSchema)
async def get_booking(booking_id: int, user: Users = Depends(get_current_user)):
    booking = await BookingDAO.find_by_id(booking_id)
    if not booking:
        raise BookingNotFoundExeption
    return booking

