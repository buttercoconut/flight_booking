from datetime import datetime
from typing import List

from app.models.models import Flight, Airline, Booking, Payment
from app.schemas.schemas import FlightSearchRequest

# In-memory data store for demo purposes
airlines = [Airline(id=1, name="SkyHigh", country="USA"), Airline(id=2, name="FlyAway", country="UK")]
flights = [
    Flight(
        id=1,
        airline_id=1,
        flight_number="SH123",
        departure_airport="JFK",
        arrival_airport="LAX",
        departure_time=datetime(2024, 9, 1, 8, 0),
        arrival_time=datetime(2024, 9, 1, 11, 0),
        price=199.99,
    ),
    Flight(
        id=2,
        airline_id=2,
        flight_number="FA456",
        departure_airport="LHR",
        arrival_airport="CDG",
        departure_time=datetime(2024, 9, 1, 9, 30),
        arrival_time=datetime(2024, 9, 1, 11, 0),
        price=89.99,
    ),
]

async def search_flights(request: FlightSearchRequest) -> List[Flight]:
    # Simple filter logic; in real app query DB
    results = [f for f in flights if f.departure_airport == request.origin and f.arrival_airport == request.destination]
    return results
