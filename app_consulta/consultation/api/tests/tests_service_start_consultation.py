from uuid import UUID

from django.test import TestCase

from api.dto.start_consultation_parameter_dto import StartConsultationParameterDto
from api.service.start_consultation_service import StartConsultationService


class ServiceStartConsultationTest(TestCase):

    def test_service_start(self):
        service = StartConsultationService()
        dto = StartConsultationParameterDto(physician_id=UUID("ea959b03-5577-45c9-b9f7-a45d3e77ce82"),
                                            patient_id=UUID("86158d46-ce33-4e3d-9822-462bbff5782e"))
        consultation = service.begin(dto)
        self.assertEqual(consultation.physician_id, UUID("ea959b03-5577-45c9-b9f7-a45d3e77ce82"))
