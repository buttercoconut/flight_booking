from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

class Airline(BaseModel):
    id: int
    name: str
    country: Optional[str] = None

class Flight(BaseModel):
    id: int
    airline_id: int
    flight_number: str
    departure_airport: str
    arrival_airport: str
    departure_time: datetime
    arrival_time: datetime
    price: float

class User(BaseModel):
    id: int
    email: str
    full_name: Optional[str] = None
    hashed_password: str

class Booking(BaseModel):
    id: int
    user_id: int
    flight_id: int
    passengers: int
    status: str
    created_at: datetime

class Payment(BaseModel):
    id: int
    booking_id: int
    amount: float
    method: str
    status: str
    paid_at: Optional[datetime] = None
