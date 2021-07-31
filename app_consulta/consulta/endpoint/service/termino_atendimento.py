import logging

from endpoint.models.consulta import Consulta
from endpoint.repository.consulta_repository import ConsultaRepository


class TerminoAtendimento:
    """ Encerra o atendimento de uma consulta """

    repository = ConsultaRepository()
    logger = logging.getLogger(__name__)

    def encerrar_encerrar(self, consulta: Consulta):
        self.logger.info(f'Consulta {consulta.id} Encerrada')