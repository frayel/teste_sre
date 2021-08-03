from decimal import Decimal
from uuid import UUID

from django.test import TestCase

from api.dto.payment_dto import PaymentDto
from api.models.payment_model import PaymentModel
from api.repository.payment_repository import PaymentRepository


class PendingPaymentRepositoryTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.pending_payment = PaymentModel(
            id=UUID("9c317dd5-a237-4e34-a059-96e7d2183aa9"),
            appointment_id=UUID("ea959b03-5577-45c9-b9f7-a45d3e77ce82"),
            total_price=Decimal(200.00),
        )
        cls.pending_payment.save()
        cls.repository = PaymentRepository()

    def test_get_by_appointment_id(self):
        uuid = UUID("ea959b03-5577-45c9-b9f7-a45d3e77ce82")
        dto = self.repository.get_by_appointment_id(uuid)
        self.assertEqual(dto, self.pending_payment.to_dto())

    def test_is_recorded(self):
        uuid = UUID("ea959b03-5577-45c9-b9f7-a45d3e77ce82")
        result = self.repository.is_recorded(uuid)
        self.assertTrue(result)

    def test_save(self):
        dto = PaymentDto(
            appointment_id=UUID("22222222-2222-2222-2222-222222222222"),
            total_price=Decimal(200.00),
        )
        saved = self.repository.save(dto)
        self.assertIsNotNone(saved.id)
        self.assertEqual(dto, saved)
