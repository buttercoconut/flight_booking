from pydantic import BaseModel

class BookingBase(BaseModel):
    flight_id: int
    seat_number: str

class BookingCreate(BookingBase):
    pass

class BookingRead(BookingBase):
    id: int
    status: str

    class Config:
        orm_mode = True
