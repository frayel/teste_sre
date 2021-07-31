from django.test import TestCase

from endpoint.dto.inicio_consulta_dto import InicioConsultaDto
from endpoint.service.inicio_atendimento import InicioAtendimento


class ServiceInicioAtendimento(TestCase):

    def test_service_iniciar(self):
        service = InicioAtendimento()
        dto = InicioConsultaDto(physician_id="ea959b03-5577-45c9-b9f7-a45d3e77ce82",
                                patient_id="86158d46-ce33-4e3d-9822-462bbff5782e")
        consulta = service.iniciar_atendimento(dto)
        self.assertEqual(consulta.physician_id, "ea959b03-5577-45c9-b9f7-a45d3e77ce82")
