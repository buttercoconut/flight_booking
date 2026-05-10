from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..services.payment_service import PaymentService
from ..schemas.payment import PaymentCreate, PaymentRead

router = APIRouter()

# Dependency to get DB session
from ..database import get_db

@router.post("/", response_model=PaymentRead)
async def pay(payment_in: PaymentCreate, db: Session = Depends(get_db)):
    service = PaymentService(db)
    return service.process_payment(payment_in)

@router.get("/{booking_id}")
async def get_payment(booking_id: int, db: Session = Depends(get_db)):
    service = PaymentService(db)
    payment = service.db.query(Payment).filter(Payment.booking_id == booking_id).first()
    if not payment:
        raise HTTPException(status_code=404, detail="Payment not found")
    return payment
