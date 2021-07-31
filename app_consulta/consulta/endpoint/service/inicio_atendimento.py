import logging

from endpoint.dto.inicio_consulta_dto import InicioConsultaDto
from endpoint.models.consulta import Consulta
from endpoint.repository.consulta_repository import ConsultaRepository


class InicioAtendimento:
    """ Inicia o atendimento de uma consulta """
    repository = ConsultaRepository()
    logger = logging.getLogger(__name__)

    def iniciar_atendimento(self, dto: InicioConsultaDto):
        consulta = Consulta(physician_id=dto.physician_id, patient_id=dto.patient_id)

        # Verificar se o paciente ou medico ja esta em consulta

        self.repository.save(consulta)
        self.logger.info(f"Consulta {consulta.id} Iniciada às {consulta.start_date}")
        return consulta
