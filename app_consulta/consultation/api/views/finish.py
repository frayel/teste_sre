import logging

from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.exceptions.invalid_data import InvalidDataException
from api.exceptions.invalid_operation import InvalidOperationException
from api.service.finish_consultation_service import FinishConsultationService
from api.service.handler_consultation import HandlerConsultation
from api.service.start_consultation_service import StartConsultationService


class FinishConsutationView(APIView):
    """ View para término de uma consulta
        url: /app/consultation/finish/ """

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    finish = FinishConsultationService()
    handler = HandlerConsultation()

    def post(self, request):
        logging.info(f"API IniciarConsulta acessada por {request.user.username}")

        try:
            dto = self.handler.finish_consultation_from_text(request.body)
            consultation = self.finish.end(dto)

        except InvalidDataException as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        except InvalidOperationException as e:
            logging.exception("Ocorreu uma operação inválida ao encerrar a consulta.")
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        return Response(f"Consulta {consultation.id} Encerrada às {consultation.end_date}", status=status.HTTP_202_ACCEPTED)