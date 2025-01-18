from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from sqlalchemy import select, update, delete
from app.hotels.schemas import HotelCreateSchema, HotelResponseSchema, HotelUpdateImageSchema, HotelUpdateServicesSchema, HotelUpdateRoomQuantitySchema, HotelUpdate
from app.hotels.dao import HotelDAO
from app.users.schemas import UserResponseSchema
from app.auth.dependencies import get_current_user
from app.exceptions import HotelAlreadyExistsExeption, HotelNotFoundExeption
from app.hotels.models import Hotels
from app.database import async_session_maker


router = APIRouter(
    prefix="/hotels",
    tags=["Hotels"]
)


@router.get("/all", response_model=list[HotelResponseSchema], status_code=200)
async def get_all_hotels():
    return await HotelDAO.find_all()

@router.get("/{hotel_id}", response_model=HotelCreateSchema, status_code=200)
async def get_hotel_by_id(hotel_id: int):

    return await HotelDAO.find_by_id(hotel_id)


@router.post("/add", response_model=HotelCreateSchema, status_code=201)
async def add_hotel(hotel_data: HotelCreateSchema, current_user: UserResponseSchema = Depends(get_current_user)):
    existing_hotel = await HotelDAO.find_by_filter(name=hotel_data.name)
    if existing_hotel:
        raise HotelAlreadyExistsExeption
    new_hotel= await HotelDAO.add(name=hotel_data.name,
                                location=hotel_data.location,
                                services=hotel_data.services,
                                rooms_quantity=hotel_data.rooms_quantity,
                                image_id=hotel_data.image_id)
    return new_hotel


@router.patch("/update_image/{hotel_id}", response_model=HotelResponseSchema)
async def update_hotel_images(hotel_id: int, hotel_update_image: HotelUpdateImageSchema):
    async with async_session_maker() as session:
        existing_hotel = await HotelDAO.find_by_filter(id=hotel_id)
        if not existing_hotel:
            raise HotelAlreadyExistsExeption
        
        query = update(Hotels).where(Hotels.id==hotel_id).values(hotel_update_image.model_dump()).returning(Hotels.__table__.columns)
        new_hotel = await session.execute(query)
        await session.commit()
        return new_hotel.mappings().one()


@router.patch("/update_services/{hotel_id}", response_model=HotelResponseSchema)
async def update_hotel_services(hotel_id: int, hotel_update_services: HotelUpdateServicesSchema):
    async with async_session_maker() as session:
        existing_hotel = await HotelDAO.find_by_filter(id=hotel_id)
        if not existing_hotel:
            raise HotelAlreadyExistsExeption
        
        query = update(Hotels).where(Hotels.id==hotel_id).values(hotel_update_services.model_dump()).returning(Hotels.__table__.columns)
        new_hotel = await session.execute(query)
        await session.commit()
        return new_hotel.mappings().one()


@router.patch("/update_room_quan/{hotel_id}", response_model=HotelResponseSchema)
async def update_hotel_room_quan(hotel_id: int, hotel_update_room_quan: HotelUpdateRoomQuantitySchema):
    async with async_session_maker() as session:
        existing_hotel = await HotelDAO.find_by_filter(id=hotel_id)
        if not existing_hotel:
            raise HotelAlreadyExistsExeption
        
        query = update(Hotels).where(Hotels.id==hotel_id).values(hotel_update_room_quan.model_dump()).returning(Hotels.__table__.columns)
        new_hotel = await session.execute(query)
        await session.commit()
        return new_hotel.mappings().one()


@router.put("/update_img_room_services/{hotel_id}", response_model=HotelResponseSchema)
async def update_hotel_img_room_services(hotel_id: int, hotel_img_room_services: HotelUpdate):
    async with async_session_maker() as session:
        existing_hotel = await HotelDAO.find_by_filter(id=hotel_id)
        if not existing_hotel:
            raise HotelAlreadyExistsExeption
        
        query = update(Hotels).where(Hotels.id==hotel_id).values(hotel_img_room_services.model_dump()).returning(Hotels.__table__.columns)
        new_hotel = await session.execute(query)
        await session.commit()
        return new_hotel.mappings().one()


@router.delete("/delete/{hotel_id}", response_model=HotelResponseSchema, status_code=202)
async def delete_hotel_by_id(hotel_id: int):
    return await HotelDAO.delete(hotel_id)