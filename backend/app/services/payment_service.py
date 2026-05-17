from datetime import datetime
from typing import List

from app.models.models import Payment
from app.schemas.schemas import PaymentRequest

# In-memory payment store
payments: List[Payment] = []

async def process_payment(request: PaymentRequest) -> Payment:
    new_id = len(payments) + 1
    payment = Payment(
        id=new_id,
        booking_id=request.booking_id,
        amount=0.0,  # would look up booking price
        method=request.method,
        status="paid",
        paid_at=datetime.utcnow(),
    )
    payments.append(payment)
    return payment
