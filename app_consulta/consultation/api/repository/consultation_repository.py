from api.models.consultation_model import ConsultationModel


class ConsultationRepository:
    """ Acesso ao model do objeto Consulta """

    objects = ConsultationModel.objects

    def get_by_consultation_id(self, pk: str) -> ConsultationModel:
        return self.objects.get(id=pk)

    def is_patient_in_consultation(self, patient_id: str) -> bool:
        return self.objects.filter(patient_id=patient_id).count() > 0

    def save(self, consultation: ConsultationModel) -> None:
        consultation.save()

    def save_finish(self, consultation: ConsultationModel) -> None:
        consultation.save(update_fields=["end_date", "price"])