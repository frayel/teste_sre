from uuid import UUID


class FinishConsultationParameterDto:
    """ Objeto de parametro para api de termino de consulta """

    def __init__(self, consultation_id: UUID) -> None:
        self.consultation_id = consultation_id
