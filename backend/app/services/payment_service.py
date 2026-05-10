from sqlalchemy.orm import Session
from ..models.payment import Payment
from ..schemas.payment import PaymentCreate, PaymentRead

class PaymentService:
    def __init__(self, db: Session):
        self.db = db

    def process_payment(self, payment_in: PaymentCreate) -> PaymentRead:
        payment = Payment(**payment_in.dict())
        self.db.add(payment)
        self.db.commit()
        self.db.refresh(payment)
        return payment
