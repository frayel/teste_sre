from decimal import Decimal
from unittest.mock import patch
from uuid import UUID

from django.test import TestCase

from api.models.pending_payment_model import PendingPaymentModel
from api.service.process_payment_service import ProcessPaymentService


class RemotePaymentServiceTest(TestCase):

    pending_payment: PendingPaymentModel

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

    @patch('api.service.remote.remote_payment_service.requests.post')
    def test_process(self, mock_send):
        mock_send.return_value.status_code = 200
        service = ProcessPaymentService()
        service.process()
        pending = PendingPaymentModel.objects.get(id=self.pending_payment.id)
        self.assertTrue(pending.finished)
