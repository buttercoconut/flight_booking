"""Payment schema definitions.
"""

from pydantic import BaseModel, Field
from typing import Literal

class PaymentRequest(BaseModel):
    amount: float
    currency: str = Field(default="USD")
    payment_method: str

class PaymentResponse(BaseModel):
    transaction_id: str
    status: Literal["success", "failed"]
    amount: float
    currency: str
