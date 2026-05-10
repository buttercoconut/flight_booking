from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..services.flight_service import FlightService
from ..schemas.flight import FlightCreate, FlightRead
from ..models.flight import Flight

router = APIRouter()

# Dependency to get DB session
from ..database import get_db

@router.post("/", response_model=FlightRead)
async def create_flight(flight_in: FlightCreate, db: Session = Depends(get_db)):
    service = FlightService(db)
    return service.create_flight(flight_in)

@router.get("/{flight_id}", response_model=FlightRead)
async def read_flight(flight_id: int, db: Session = Depends(get_db)):
    service = FlightService(db)
    flight = service.get_flight(flight_id)
    if not flight:
        raise HTTPException(status_code=404, detail="Flight not found")
    return flight

@router.get("/", response_model=list[FlightRead])
async def list_flights(db: Session = Depends(get_db)):
    service = FlightService(db)
    return service.list_flights()
