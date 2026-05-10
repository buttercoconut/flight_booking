"""Test suite for the booking service.

The tests exercise the in‑memory booking logic defined in
``backend/app/services/booking_service.py``.
"""

import pytest

from backend.app.services.booking_service import create_booking, get_booking
from backend.app.schemas.booking import BookingCreate


@pytest.fixture
def booking_request() -> BookingCreate:
    return BookingCreate(
        flight_id="AB123",
        passenger_name="John Doe",
        passenger_email="john@example.com",
        seat_preference="Aisle",
    )


def test_create_and_retrieve_booking(booking_request: BookingCreate):
    # Create a booking
    created = create_booking(booking_request)
    assert created.id is not None
    assert created.status == "confirmed"

    # Retrieve the same booking
    retrieved = get_booking(created.id)
    assert retrieved is not None
    assert retrieved.id == created.id
    assert retrieved.passenger_name == booking_request.passenger_name


def test_get_nonexistent_booking():
    assert get_booking("non‑existent‑id") is None
