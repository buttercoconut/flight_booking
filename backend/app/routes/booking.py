"""Booking router.

Handles creation of a booking and retrieval of booking details.
"""

from fastapi import APIRouter, HTTPException
from uuid import uuid4
from typing import Dict

from ..schemas.booking import BookingCreate, BookingResponse

router = APIRouter()

# In‑memory store – replace with a database in production
BOOKINGS: Dict[str, BookingResponse] = {}

@router.post("/bookings", response_model=BookingResponse)
async def create_booking(booking: BookingCreate):
    """Create a new booking.

    The booking is stored in the ``BOOKINGS`` dictionary and a unique ID
    is generated. In a real system you would persist the booking to a
    database and perform validation.
    """
    booking_id = str(uuid4())
    booking_response = BookingResponse(id=booking_id, **booking.dict())
    BOOKINGS[booking_id] = booking_response
    return booking_response

@router.get("/bookings/{booking_id}", response_model=BookingResponse)
async def get_booking(booking_id: str):
    booking = BOOKINGS.get(booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking
