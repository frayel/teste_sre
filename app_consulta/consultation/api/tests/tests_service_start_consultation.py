from django.test import TestCase

from api.dto.start_consultation_dto import StartConsultationDto
from api.service.start_consultation_service import StartConsultationService


class ServiceStartConsultationTest(TestCase):

    def test_service_start(self):
        service = StartConsultationService()
        dto = StartConsultationDto(physician_id="ea959b03-5577-45c9-b9f7-a45d3e77ce82",
                                   patient_id="86158d46-ce33-4e3d-9822-462bbff5782e")
        consultation = service.begin(dto)
        self.assertEqual(consultation.physician_id, "ea959b03-5577-45c9-b9f7-a45d3e77ce82")
