from decimal import Decimal
from uuid import UUID

from django.test import TestCase

from api.dto.payment_dto import PaymentDto
from api.service.payment_service import PaymentService


class ServicePaymentTest(TestCase):

    def test_service_record(self):
        service = PaymentService()
        dto = PaymentDto(appointment_id=UUID("84ab6121-c4a8-4684-8cc2-b03024ec0f1d"), total_price=Decimal(200.00))
        payment = service.record(dto)
        self.assertEqual(payment.appointment_id, UUID("84ab6121-c4a8-4684-8cc2-b03024ec0f1d"))
