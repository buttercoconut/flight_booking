"""Payment router.

Provides a stub endpoint for processing payments. In a real application
this would integrate with a payment gateway such as Stripe or PayPal.
"""

from fastapi import APIRouter, HTTPException
from uuid import uuid4

from ..schemas.payment import PaymentRequest, PaymentResponse

router = APIRouter()

@router.post("/payments", response_model=PaymentResponse)
async def process_payment(payment: PaymentRequest):
    """Simulate payment processing.

    The endpoint simply returns a success response with a mock transaction
    ID. Replace this logic with real payment gateway integration.
    """
    # Basic validation – ensure amount is positive
    if payment.amount <= 0:
        raise HTTPException(status_code=400, detail="Amount must be positive")

    transaction_id = str(uuid4())
    return PaymentResponse(
        transaction_id=transaction_id,
        status="success",
        amount=payment.amount,
        currency=payment.currency,
    )
