"""Main entry point for the FastAPI application.

This file sets up the FastAPI instance, mounts the API router under the
``/api`` prefix, and includes basic configuration such as CORS middleware.

The application is intentionally lightweight – the goal is to provide a
minimal, but fully functional, backend that can be extended with additional
business logic, database integration, authentication, etc.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Import routers
from .routes.flight import router as flight_router
from .routes.booking import router as booking_router
from .routes.payment import router as payment_router

# Create FastAPI app
app = FastAPI(title="Flight Booking API", version="1.0.0")

# Allow CORS for local development (frontend runs on http://localhost:3000)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount routers under /api prefix
app.include_router(flight_router, prefix="/api")
app.include_router(booking_router, prefix="/api")
app.include_router(payment_router, prefix="/api")

# Simple health‑check endpoint
@app.get("/api/health")
async def health_check():
    return {"status": "ok"}
