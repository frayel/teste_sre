from unittest import TestCase
from uuid import UUID

from api.converter.payment_converter import PaymentConverter
from api.models.payment_model import PaymentModel


class PaymentConverterTest(TestCase):

    def test_from_model_to_dto(self):
        converter = PaymentConverter()
        model = PaymentModel(appointment_id=UUID("ea959b03-5577-45c9-b9f7-a45d3e77ce82"), total_price=200.00)
        dto = converter.from_model_to_dto(model)
        self.assertEqual(model.appointment_id, dto.appointment_id)