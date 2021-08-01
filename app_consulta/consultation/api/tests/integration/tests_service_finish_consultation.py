from uuid import UUID

from django.test import TestCase
from django.utils import timezone

from api.dto.finish_consultation_dto import FinishConsultationDto
from api.models.consultation_model import ConsultationModel
from api.service.finish_consultation_service import FinishConsultationService


class ServiceFinishConsultationTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        consultation = ConsultationModel(
            id=UUID("9c317dd5-a237-4e34-a059-96e7d2183aa9"),
            start_date=timezone.now(),
            end_date=None,
            physician_id=UUID("ea959b03-5577-45c9-b9f7-a45d3e77ce82"),
            patient_id=UUID("86158d46-ce33-4e3d-9822-462bbff5782e"),
            price=None,
        )
        consultation.save()

    def test_service_finish(self):
        service = FinishConsultationService()
        dto = FinishConsultationDto(consultation_id=UUID("9c317dd5-a237-4e34-a059-96e7d2183aa9"))
        consultation = service.end(dto)
        self.assertIsNotNone(consultation.end_date)
        self.assertIsNotNone(consultation.price)
