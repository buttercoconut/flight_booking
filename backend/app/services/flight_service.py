from sqlalchemy.orm import Session
from ..models.flight import Flight
from ..schemas.flight import FlightCreate, FlightRead

class FlightService:
    def __init__(self, db: Session):
        self.db = db

    def create_flight(self, flight_in: FlightCreate) -> FlightRead:
        flight = Flight(**flight_in.dict())
        self.db.add(flight)
        self.db.commit()
        self.db.refresh(flight)
        return flight

    def get_flight(self, flight_id: int) -> FlightRead | None:
        return self.db.query(Flight).filter(Flight.id == flight_id).first()

    def list_flights(self):
        return self.db.query(Flight).all()
