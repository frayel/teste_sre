from uuid import UUID

from api.dto.consultation_dto import ConsultationDto
from api.models.consultation_model import ConsultationModel


class ConsultationRepository:
    """ Camada de persistência de dados da Consulta """

    def __init__(self):
        self.objects = ConsultationModel.objects

    def get_by_consultation_id(self, pk: UUID) -> ConsultationDto:
        """ Obtém uma consulta pelo id """
        model = self.objects.get(id=pk)
        return model.to_dto() if model else None

    def is_patient_in_consultation(self, patient_id: UUID) -> bool:
        """ Verifica se um paciente está em uma consulta não finalizada """
        return self.objects.filter(patient_id=patient_id, end_date__isnull=True).count() > 0

    def save(self, dto: ConsultationDto) -> ConsultationDto:
        """ Grava uma consulta """
        db_model = self.objects.filter(id=dto.id).first() or ConsultationModel()
        db_model.start_date = dto.start_date
        db_model.end_date = dto.end_date
        db_model.physician_id = dto.physician_id
        db_model.patient_id = dto.patient_id
        db_model.price = dto.price
        db_model.save()
        return db_model.to_dto()

    def save_finish(self, dto: ConsultationDto) -> ConsultationDto:
        """ Grava o encerramento de uma consulta """
        db_model = self.objects.get(id=dto.id)
        db_model.end_date = dto.end_date
        db_model.price = dto.price
        db_model.save(update_fields=["end_date", "price"])
        return db_model.to_dto()

