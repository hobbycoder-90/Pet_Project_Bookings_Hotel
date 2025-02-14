from fastapi import FastAPI
from appp.bookings.router import router as bookings_router
from appp.users.router import router as users_router
from appp.auth.router import router as auth_router
from appp.hotels.router import router as hotels_router


app = FastAPI(
    title="FastAPI PetProject Bookings Hotel",
    version="0.1",
    description="This is a very fancy project, with auto docs for the API and everything",
)


app.include_router(auth_router)
app.include_router(users_router)
app.include_router(hotels_router)
app.include_router(bookings_router)

#if __name__ == "__main__":
#    uvicorn.run(
#        app="main:app",
#        reload=True,
#    ) 

