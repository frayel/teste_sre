from decimal import Decimal
from uuid import UUID

from django.test import TestCase
from django.utils import timezone

from api.dto.consultation_dto import ConsultationDto
from api.models.consultation_model import ConsultationModel
from api.repository.consultation_repository import ConsultationRepository


class ConsultationRepositoryTest(TestCase):

    consultation: ConsultationModel

    @classmethod
    def setUpTestData(cls):
        cls.consultation = ConsultationModel(
            id=UUID("9c317dd5-a237-4e34-a059-96e7d2183aa9"),
            start_date=timezone.now(),
            end_date=None,
            physician_id=UUID("ea959b03-5577-45c9-b9f7-a45d3e77ce82"),
            patient_id=UUID("86158d46-ce33-4e3d-9822-462bbff5782e"),
            price=None,
        )
        cls.consultation.save()
        cls.repository = ConsultationRepository()

    def test_get_by_consultation_id(self):
        uuid = UUID("9c317dd5-a237-4e34-a059-96e7d2183aa9")
        dto = self.repository.get_by_consultation_id(uuid)
        self.assertEqual(dto, self.consultation.to_dto())

    def test_is_patient_in_consultation(self):
        uuid = UUID("9c317dd5-a237-4e34-a059-96e7d2183aa9")
        result = self.repository.is_patient_in_consultation(uuid)
        self.assertEqual(result, False)

    def test_save(self):
        dto = ConsultationDto(
            start_date=timezone.now(),
            physician_id=UUID("11111111-1111-1111-1111-111111111111"),
            patient_id=UUID("22222222-2222-2222-2222-222222222222"),
        )
        saved = self.repository.save(dto)
        self.assertIsNotNone(saved.id)
        self.assertEqual(dto, saved)

    def test_save_finish(self):
        dto = ConsultationDto(
            id=UUID("9c317dd5-a237-4e34-a059-96e7d2183aa9"),
            end_date=timezone.now(),
            price=Decimal(999.99)
        )
        saved = self.repository.save_finish(dto)
        self.assertIsNotNone(saved.id)
        self.assertEqual(dto, saved)