from uuid import UUID


class StartConsultationParameterDto:
    """ Objeto de parametro para api de início de consulta """

    def __init__(self, physician_id: UUID, patient_id: UUID) -> None:
        self.physician_id = physician_id
        self.patient_id = patient_id
