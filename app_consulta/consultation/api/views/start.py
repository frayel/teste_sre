import logging

from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.exceptions.invalid_data import InvalidDataException
from api.exceptions.invalid_operation import InvalidOperationException
from api.service.handler_consultation import HandlerConsultation
from api.service.start_consultation_service import StartConsultationService


class StartConsutationView(APIView):
    """ View para início de uma consulta
        url: /app/consultation/start/ """

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    start = StartConsultationService()
    handler = HandlerConsultation()

    def post(self, request):
        logging.info(f"API IniciarConsulta acessada por {request.user.username}")

        try:
            dto = self.handler.start_consultation_from_text(request.body)
            consultation = self.start.begin(dto)

        except InvalidDataException as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        except InvalidOperationException as e:
            logging.exception("Ocorreu uma operação inválida ao iniciar a consulta.")
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        return Response(f"Consulta {consultation.id} Iniciada às {consultation.start_date}", status=status.HTTP_201_CREATED)