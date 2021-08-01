from uuid import UUID


class StartConsultationDto:
    """ Objeto de entrada para api de início de consulta """

    def __init__(self, physician_id: UUID, patient_id: UUID) -> None:
        self.physician_id = physician_id
        self.patient_id = patient_id
