import logging

from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from endpoint.service.handler_consulta import HandlerConsulta
from endpoint.service.inicio_atendimento import InicioAtendimento


class IniciarConsulta(APIView):
    """ View para início de uma consulta
        url: /app/consulta/iniciar/ """

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    logger = logging.getLogger(__name__)
    inicio_atendimento = InicioAtendimento()
    handler_consulta = HandlerConsulta()

    def post(self, request):
        self.logger.info(f"API IniciarConsulta acessada por {request.user.username}")

        try:
            dto = self.handler_consulta.inicio_consulta_from_text(request.body)
            consulta = self.inicio_atendimento.iniciar_atendimento(dto)

        except Exception as e:
            self.logger.exception("Ocorreu um erro ao iniciar a consulta.")
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        return Response(f"Consulta {consulta.id} Iniciada às {consulta.start_date}", status=status.HTTP_201_CREATED)