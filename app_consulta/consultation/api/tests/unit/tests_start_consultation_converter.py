from unittest import TestCase
from uuid import UUID

from api.converter.start_consultation_converter import StartConsultationConverter


class StartConsultationConverterTest(TestCase):

    def test_start_consultation_from_text(self):
        converter = StartConsultationConverter()
        data = '{"physician_id": "ea959b03-5577-45c9-b9f7-a45d3e77ce82", "patient_id": "86158d46-ce33-4e3d-9822-462bbff5782e"}'
        dto = converter.from_text(data)
        self.assertEqual(dto.physician_id, UUID("ea959b03-5577-45c9-b9f7-a45d3e77ce82"))
        self.assertEqual(dto.patient_id, UUID("86158d46-ce33-4e3d-9822-462bbff5782e"))
