from fastapi import FastAPI
from app.routes import flight, booking, payment

app = FastAPI(title="Flight Booking API")

app.include_router(flight.router, prefix="/flights", tags=["flights"])
app.include_router(booking.router, prefix="/bookings", tags=["bookings"])
app.include_router(payment.router, prefix="/payments", tags=["payments"])

@app.get("/")
async def root():
    return {"message": "Welcome to Flight Booking API"}
