import logging

from api.dto.start_consultation_dto import StartConsultationDto
from api.exceptions.invalid_operation import InvalidOperationException
from api.models.consultation_model import ConsultationModel
from api.repository.consultation_repository import ConsultationRepository


class StartConsultationService:
    """ Inicia o atendimento de uma consulta """
    consultation_repository = ConsultationRepository()

    def begin(self, dto: StartConsultationDto):
        consultation = ConsultationModel(physician_id=dto.physician_id, patient_id=dto.patient_id)

        # Verificar se o paciente ou medico ja esta em consulta
        if self.consultation_repository.is_patient_in_consultation(dto.patient_id):
            raise InvalidOperationException(f"O Paciente {dto.patient_id} já está em consulta")

        self.consultation_repository.save(consultation)
        logging.info(f"Consulta {consultation.id} Iniciada às {consultation.start_date}")
        return consultation
