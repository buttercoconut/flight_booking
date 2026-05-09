"""Booking schema definitions.
"""

from pydantic import BaseModel, Field
from typing import Optional

class BookingCreate(BaseModel):
    flight_id: str
    passenger_name: str
    passenger_email: str
    seat_preference: Optional[str] = None

class BookingResponse(BookingCreate):
    id: str
    status: str = Field(default="confirmed")
