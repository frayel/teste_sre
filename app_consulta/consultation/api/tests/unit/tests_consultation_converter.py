from unittest import TestCase
from uuid import UUID

from api.converter.consultation_converter import ConsultationConverter
from api.models.consultation_model import ConsultationModel


class ConsultationConverterTest(TestCase):

    def test_from_model_to_dto(self):
        converter = ConsultationConverter()
        model = ConsultationModel(id=UUID("ea959b03-5577-45c9-b9f7-a45d3e77ce82"))
        dto = converter.from_model_to_dto(model)
        self.assertEqual(model.id, dto.id)

    def test_start_consultation_from_text(self):
        converter = ConsultationConverter()
        data = '{"physician_id": "ea959b03-5577-45c9-b9f7-a45d3e77ce82", "patient_id": "86158d46-ce33-4e3d-9822-462bbff5782e"}'
        dto = converter.start_data_from_text(data)
        self.assertEqual(dto.physician_id, UUID("ea959b03-5577-45c9-b9f7-a45d3e77ce82"))
        self.assertEqual(dto.patient_id, UUID("86158d46-ce33-4e3d-9822-462bbff5782e"))

    def test_finish_consultation_from_text(self):
        converter = ConsultationConverter()
        data = '{"consultation_id": "ea959b03-5577-45c9-b9f7-a45d3e77ce82"}'
        dto = converter.finish_data_from_text(data)
        self.assertEqual(dto.consultation_id, UUID("ea959b03-5577-45c9-b9f7-a45d3e77ce82"))

