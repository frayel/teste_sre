from endpoint.models.consulta import Consulta


class ConsultaRepository:
    """ Acesso ao model do objeto Consulta """

    objects = Consulta.objects

    def get(self, pk: str) -> Consulta:
        return self.objects.get(id=pk)

    def save(self, consulta: Consulta) -> None:
        consulta.save()

