from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app.schemas.schemas import BookingCreateRequest, BookingResponse, PaymentRequest, PaymentResponse
from app.services.booking_service import create_booking
from app.services.payment_service import process_payment

router = APIRouter()

@router.post("/create", response_model=BookingResponse)
async def create_booking_endpoint(request: BookingCreateRequest):
    booking = await create_booking(request)
    return BookingResponse(id=booking.id, status=booking.status)
