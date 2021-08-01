from unittest import TestCase
from uuid import UUID

from api.converter.consultation_converter import ConsultationConverter
from api.dto.consultation_dto import ConsultationDto
from api.models.consultation_model import ConsultationModel


class ConsultationConverterTest(TestCase):

    def test_from_dto_to_model(self):
        converter = ConsultationConverter()
        dto = ConsultationDto(id=UUID("ea959b03-5577-45c9-b9f7-a45d3e77ce82"))
        model = converter.from_dto_to_model(dto, None)
        self.assertEqual(model.id, dto.id)

    def test_from_model_to_dto(self):
        converter = ConsultationConverter()
        model = ConsultationModel(id=UUID("ea959b03-5577-45c9-b9f7-a45d3e77ce82"))
        dto = converter.from_model_to_dto(model)
        self.assertEqual(model.id, dto.id)