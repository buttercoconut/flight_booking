"""Test suite for the payment service.

The tests exercise the stub payment logic defined in
``backend/app/services/payment_service.py``.
"""

import pytest

from backend.app.services.payment_service import process_payment
from backend.app.schemas.payment import PaymentRequest


@pytest.fixture
def payment_request() -> PaymentRequest:
    return PaymentRequest(amount=150.0, currency="USD", payment_method="credit_card")


def test_process_payment(payment_request: PaymentRequest):
    response = process_payment(payment_request)
    assert response.transaction_id is not None
    assert response.status == "success"
    assert response.amount == payment_request.amount
    assert response.currency == payment_request.currency
