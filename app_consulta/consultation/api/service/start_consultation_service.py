import logging

from api.dto.consultation_dto import ConsultationDto
from api.dto.start_consultation_dto import StartConsultationDto
from api.exceptions.invalid_operation import InvalidOperationException
from api.repository.consultation_repository import ConsultationRepository


class StartConsultationService:
    """ Serviço de início de atendimento de uma consulta """

    consultation_repository = ConsultationRepository()

    def begin(self, start_dto: StartConsultationDto) -> ConsultationDto:
        consultation_dto = ConsultationDto(physician_id=start_dto.physician_id, patient_id=start_dto.patient_id)

        # Verificar se o paciente ou medico ja esta em consulta
        if self.consultation_repository.is_patient_in_consultation(start_dto.patient_id):
            raise InvalidOperationException(f"O Paciente {start_dto.patient_id} já está em consulta")

        consultation_dto = self.consultation_repository.save(consultation_dto)
        logging.info(f"Consulta {consultation_dto.id} Iniciada às {consultation_dto.start_date}")
        return consultation_dto
