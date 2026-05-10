"""Test suite for the flight service.

The tests exercise the in‑memory flight search logic defined in
``backend/app/services/flight_service.py``.
"""

import pytest
from datetime import date

from backend.app.services.flight_service import search_flights


def test_search_flights_found():
    result = search_flights("JFK", "LAX", date(2024, 5, 10))
    assert len(result.flights) > 0
    assert result.flights[0].departure_airport == "JFK"
    assert result.flights[0].arrival_airport == "LAX"


def test_search_flights_not_found():
    result = search_flights("XYZ", "ABC", date(2024, 5, 10))
    assert len(result.flights) == 0
