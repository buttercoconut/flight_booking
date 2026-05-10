from pydantic import BaseModel, EmailStr
from datetime import datetime

class FlightBase(BaseModel):
    flight_number: str
    departure_airport: str
    arrival_airport: str
    departure_time: datetime
    arrival_time: datetime
    price: float

class FlightCreate(FlightBase):
    airline_id: int

class FlightRead(FlightBase):
    id: int
    airline_id: int

    class Config:
        orm_mode = True
