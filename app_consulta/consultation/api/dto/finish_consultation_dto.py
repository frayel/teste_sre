from uuid import UUID


class FinishConsultationDto:
    """ Objeto de entrada para api de termino de consulta """

    def __init__(self, consultation_id: UUID) -> None:
        self.consultation_id = consultation_id
