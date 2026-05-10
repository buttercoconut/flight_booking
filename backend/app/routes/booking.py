from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..services.booking_service import BookingService
from ..schemas.booking import BookingCreate, BookingRead

router = APIRouter()

# Dependency to get DB session
from ..database import get_db

@router.post("/", response_model=BookingRead)
async def create_booking(booking_in: BookingCreate, db: Session = Depends(get_db)):
    service = BookingService(db)
    return service.create_booking(booking_in)

@router.get("/{booking_id}", response_model=BookingRead)
async def read_booking(booking_id: int, db: Session = Depends(get_db)):
    service = BookingService(db)
    booking = service.get_booking(booking_id)
    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    return booking

@router.get("/user/{user_id}", response_model=list[BookingRead])
async def list_user_bookings(user_id: int, db: Session = Depends(get_db)):
    service = BookingService(db)
    return service.list_bookings(user_id)
