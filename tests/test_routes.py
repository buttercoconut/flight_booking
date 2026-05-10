"""Test suite for the FastAPI routes.

These tests use the FastAPI test client to exercise the public API
endpoints defined in ``backend/app/routes``.
"""

import pytest
from fastapi.testclient import TestClient

from backend.app.main import app

client = TestClient(app)


def test_search_flights_endpoint():
    response = client.get("/api/flights", params={"origin": "JFK", "destination": "LAX", "date": "2024-05-10"})
    assert response.status_code == 200
    data = response.json()
    assert "flights" in data
    assert len(data["flights"]) > 0


def test_create_booking_endpoint():
    payload = {
        "flight_id": "AB123",
        "passenger_name": "Alice",
        "passenger_email": "alice@example.com",
        "seat_preference": "Window",
    }
    response = client.post("/api/bookings", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] is not None
    assert data["status"] == "confirmed"


def test_process_payment_endpoint():
    payload = {
        "amount": 200.0,
        "currency": "USD",
        "payment_method": "credit_card",
    }
    response = client.post("/api/payments", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert data["transaction_id"] is not None
    assert data["status"] == "success"
