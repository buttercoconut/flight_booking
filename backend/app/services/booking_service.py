from datetime import datetime
from typing import List

from app.models.models import Booking
from app.schemas.schemas import BookingCreateRequest

# In-memory booking store
bookings: List[Booking] = []

async def create_booking(request: BookingCreateRequest) -> Booking:
    new_id = len(bookings) + 1
    booking = Booking(
        id=new_id,
        user_id=request.user_id,
        flight_id=request.flight_id,
        passengers=request.passengers,
        status="confirmed",
        created_at=datetime.utcnow(),
    )
    bookings.append(booking)
    return booking
