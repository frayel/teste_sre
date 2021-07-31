
class InicioConsultaDto:
    def __init__(self, physician_id: str, patient_id: str) -> None:
        self.physician_id = physician_id
        self.patient_id = patient_id
