from uuid import UUID

from api.dto.consultation_dto import ConsultationDto
from api.models.consultation_model import ConsultationModel
from api.converter.consultation_converter import ConsultationConverter


class ConsultationRepository:
    """ Camada de persistência ao dados da Consulta """

    objects = ConsultationModel.objects
    converter = ConsultationConverter()

    def get_by_consultation_id(self, pk: UUID) -> ConsultationDto:
        return self.converter.from_model_to_dto(self.objects.get(id=pk))

    def is_patient_in_consultation(self, patient_id: UUID) -> bool:
        return self.objects.filter(patient_id=patient_id, end_date__isnull=True).count() > 0

    def save(self, dto: ConsultationDto) -> ConsultationDto:
        db_model = self.objects.filter(id=dto.id).first() or ConsultationModel()
        db_model.start_date = dto.start_date
        db_model.end_date = dto.end_date
        db_model.physician_id = dto.physician_id
        db_model.patient_id = dto.patient_id
        db_model.price = dto.price
        db_model.save()

        return self.converter.from_model_to_dto(db_model)

    def save_finish(self, dto: ConsultationDto) -> ConsultationDto:
        db_model = self.objects.get(id=dto.id)
        db_model.end_date = dto.end_date
        db_model.price = dto.price
        db_model.save(update_fields=["end_date", "price"])
        return self.converter.from_model_to_dto(db_model)

