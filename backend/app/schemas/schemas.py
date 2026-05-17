from pydantic import BaseModel, Field
from datetime import datetime

class FlightSearchRequest(BaseModel):
    origin: str
    destination: str
    departure_date: datetime
    passengers: int = Field(..., gt=0)

class FlightSearchResponse(BaseModel):
    flights: list

class BookingCreateRequest(BaseModel):
    user_id: int
    flight_id: int
    passengers: int

class BookingResponse(BaseModel):
    id: int
    status: str

class PaymentRequest(BaseModel):
    booking_id: int
    method: str
    card_number: Optional[str] = None
    expiry: Optional[str] = None
    cvv: Optional[str] = None

class PaymentResponse(BaseModel):
    id: int
    status: str
    paid_at: datetime
