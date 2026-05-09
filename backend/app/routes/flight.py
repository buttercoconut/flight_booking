"""Flight search router.

Provides endpoints for searching available flights. In a real application this
would query a database or an external flight data provider. For the purpose
of this template we return a static list of flights.
"""

from fastapi import APIRouter, Query
from typing import List
from datetime import date

from ..schemas.flight import FlightSearchResponse, Flight

router = APIRouter()

# Dummy data – in a real system this would come from a database
DUMMY_FLIGHTS = [
    {
        "flight_number": "AB123",
        "departure_airport": "JFK",
        "arrival_airport": "LAX",
        "departure_time": "2024-07-01T08:00:00Z",
        "arrival_time": "2024-07-01T11:00:00Z",
        "price": 350.0,
    },
    {
        "flight_number": "CD456",
        "departure_airport": "JFK",
        "arrival_airport": "SFO",
        "departure_time": "2024-07-01T09:00:00Z",
        "arrival_time": "2024-07-01T12:30:00Z",
        "price": 400.0,
    },
]

@router.get("/flights", response_model=FlightSearchResponse)
async def search_flights(
    origin: str = Query(..., description="IATA code of departure airport"),
    destination: str = Query(..., description="IATA code of arrival airport"),
    departure_date: date = Query(..., description="Date of departure"),
    return_date: date | None = Query(None, description="Optional return date for round‑trip"),
):
    """Return a list of flights matching the search criteria.

    The implementation simply filters the ``DUMMY_FLIGHTS`` list. In a
    production system you would perform a database query or call an
    external API.
    """
    # Filter by origin/destination – ignore dates for demo purposes
    results = [Flight(**f) for f in DUMMY_FLIGHTS if f["departure_airport"] == origin and f["arrival_airport"] == destination]
    return FlightSearchResponse(flights=results)
