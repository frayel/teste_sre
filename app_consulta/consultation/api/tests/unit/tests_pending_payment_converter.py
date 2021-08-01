from unittest import TestCase
from uuid import UUID

from api.converter.pending_payment_converter import PendingPaymentConverter
from api.models.pending_payment_model import PendingPaymentModel


class PendingPaymentConverterTest(TestCase):

    def test_from_model_to_dto(self):
        converter = PendingPaymentConverter()
        model = PendingPaymentModel(appointment_id=UUID("ea959b03-5577-45c9-b9f7-a45d3e77ce82"))
        dto = converter.from_model_to_dto(model)
        self.assertEqual(model.appointment_id, dto.appointment_id)