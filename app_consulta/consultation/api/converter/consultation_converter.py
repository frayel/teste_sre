from api.dto.consultation_dto import ConsultationDto
from api.models.consultation_model import ConsultationModel
from api.converter.base_converter import BaseConverter


class ConsultationConverter(BaseConverter):
    """ Converte dados da Consulta entre Model e DTO
    """

    def from_dto_to_model(self, dto: ConsultationDto, model: ConsultationModel) -> ConsultationModel:
        """ Transforma um DTO em um objeto Model """
        if not model:
            model = ConsultationModel(id=dto.id)
        model.start_date = dto.start_date
        model.end_date = dto.end_date
        model.physician_id = dto.physician_id
        model.patient_id = dto.patient_id
        model.price = dto.price
        return model

    def from_model_to_dto(self, model: ConsultationModel) -> ConsultationDto:
        """ Transforma um objeto Model em um DTO """
        dto = ConsultationDto(
            id=model.id,
            start_date=model.start_date,
            end_date=model.end_date,
            physician_id=model.physician_id,
            patient_id=model.patient_id,
            price=model.price,
        ) if model else None
        return dto

