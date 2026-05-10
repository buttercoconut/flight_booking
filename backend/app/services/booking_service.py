from sqlalchemy.orm import Session
from ..models.booking import Booking
from ..schemas.booking import BookingCreate, BookingRead

class BookingService:
    def __init__(self, db: Session):
        self.db = db

    def create_booking(self, booking_in: BookingCreate) -> BookingRead:
        booking = Booking(**booking_in.dict())
        self.db.add(booking)
        self.db.commit()
        self.db.refresh(booking)
        return booking

    def get_booking(self, booking_id: int) -> BookingRead | None:
        return self.db.query(Booking).filter(Booking.id == booking_id).first()

    def list_bookings(self, user_id: int):
        return self.db.query(Booking).filter(Booking.user_id == user_id).all()
