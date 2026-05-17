from fastapi import APIRouter, Depends, HTTPException
from typing import List

from app.schemas.schemas import PaymentRequest, PaymentResponse
from app.services.payment_service import process_payment

router = APIRouter()

@router.post("/pay", response_model=PaymentResponse)
async def payment_endpoint(request: PaymentRequest):
    payment = await process_payment(request)
    return PaymentResponse(id=payment.id, status=payment.status, paid_at=payment.paid_at)
