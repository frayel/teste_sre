from decimal import Decimal
from uuid import UUID

from django.test import TestCase

from api.dto.pending_payment_dto import PendingPaymentDto
from api.models.pending_payment_model import PendingPaymentModel
from api.repository.pending_payment_repository import PendingPaymentRepository


class PendingPaymentRepositoryTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.pending_payment = PendingPaymentModel(
            id=UUID("9c317dd5-a237-4e34-a059-96e7d2183aa9"),
            appointment_id=UUID("ea959b03-5577-45c9-b9f7-a45d3e77ce82"),
            total_price=Decimal(200.00),
            tries=0,
            processing=False,
            finished=False,
        )
        cls.pending_payment.save()
        cls.repository = PendingPaymentRepository()

    def test_get_by_appointment_id(self):
        uuid = UUID("ea959b03-5577-45c9-b9f7-a45d3e77ce82")
        dto = self.repository.get_by_appointment_id(uuid)
        self.assertEqual(dto, self.pending_payment.to_dto())

    def test_get_process_pending(self):
        lista = self.repository.get_process_pending()
        self.assertGreaterEqual(len(lista), 1)

    def test_save(self):
        dto = PendingPaymentDto(
            appointment_id=UUID("22222222-2222-2222-2222-222222222222"),
            total_price=Decimal(200.00),
            tries=0,
            processing=False,
            finished=False,
        )
        saved = self.repository.save(dto)
        self.assertIsNotNone(saved.id)
        self.assertEqual(dto, saved)

    def test_finish(self):
        uuid = UUID("ea959b03-5577-45c9-b9f7-a45d3e77ce82")
        saved = self.repository.finish(uuid)
        self.assertTrue(saved.finished)

    def test_reset_processing_flag(self):
        uuid = UUID("ea959b03-5577-45c9-b9f7-a45d3e77ce82")
        dto = self.repository.get_by_appointment_id(uuid)
        dto.processing = True
        self.repository.save(dto)
        self.repository.reset_processing_flag()
        dto = self.repository.get_by_appointment_id(uuid)
        self.assertFalse(dto.processing)