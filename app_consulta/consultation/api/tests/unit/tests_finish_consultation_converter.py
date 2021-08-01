from unittest import TestCase
from uuid import UUID

from api.converter.finish_consultation_converter import FinishConsultationConverter


class FinishConsultationConverterTest(TestCase):

    def test_finish_consultation_from_text(self):
        converter = FinishConsultationConverter()
        data = '{"consultation_id": "ea959b03-5577-45c9-b9f7-a45d3e77ce82"}'
        dto = converter.from_text(data)
        self.assertEqual(dto.consultation_id, UUID("ea959b03-5577-45c9-b9f7-a45d3e77ce82"))
