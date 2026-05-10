from pydantic import BaseModel

class PaymentBase(BaseModel):
    booking_id: int
    amount: float
    method: str

class PaymentCreate(PaymentBase):
    pass

class PaymentRead(PaymentBase):
    id: int
    status: str

    class Config:
        orm_mode = True
