"""Flight schema definitions.

These Pydantic models are used for request/response validation.
"""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import List

class Flight(BaseModel):
    flight_number: str
    departure_airport: str
    arrival_airport: str
    departure_time: datetime
    arrival_time: datetime
    price: float

class FlightSearchResponse(BaseModel):
    flights: List[Flight]
