from fastapi import APIRouter, Depends, HTTPException
from datetime import datetime
from typing import List

from app.schemas.schemas import FlightSearchRequest, FlightSearchResponse, BookingCreateRequest, BookingResponse, PaymentRequest, PaymentResponse
from app.services.flight_service import search_flights
from app.services.booking_service import create_booking
from app.services.payment_service import process_payment

router = APIRouter()

@router.post("/search", response_model=FlightSearchResponse)
async def search_flights_endpoint(request: FlightSearchRequest):
    flights = await search_flights(request)
    return FlightSearchResponse(flights=flights)

@router.post("/create", response_model=BookingResponse)
async def create_booking_endpoint(request: BookingCreateRequest):
    booking = await create_booking(request)
    return BookingResponse(id=booking.id, status=booking.status)

@router.post("/pay", response_model=PaymentResponse)
async def payment_endpoint(request: PaymentRequest):
    payment = await process_payment(request)
    return PaymentResponse(id=payment.id, status=payment.status, paid_at=payment.paid_at)
