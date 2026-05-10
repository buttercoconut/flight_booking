"""FastAPI application entry point."""

from fastapi import FastAPI
from .routes import flight, booking, payment

app = FastAPI(title="Flight Booking API")

app.include_router(flight.router, prefix="/flights", tags=["flights"])
app.include_router(booking.router, prefix="/bookings", tags=["bookings"])
app.include_router(payment.router, prefix="/payments", tags=["payments"])

# Simple health check
@app.get("/health")
async def health_check():
    return {"status": "ok"}
