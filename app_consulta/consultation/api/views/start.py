import logging

from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.exceptions.invalid_data import InvalidDataException
from api.exceptions.invalid_operation import InvalidOperationException
from api.service.start_consultation_service import StartConsultationService
from api.converter.start_consultation_converter import StartConsultationConverter


class StartConsutationView(APIView):
    """ View para início de uma consulta
        url: /app/consultation/start/ """

    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    start = StartConsultationService()
    converter = StartConsultationConverter()

    def post(self, request):
        logging.info(f"API consultation.start acessada por {request.user.username}")

        try:
            dto = self.converter.from_text(request.body)
            consultation_dto = self.start.begin(dto)

        except InvalidDataException as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        except InvalidOperationException as e:
            logging.exception("Ocorreu uma operação inválida ao iniciar a consulta.")
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        return Response(f"Consulta {consultation_dto.id} Iniciada às {consultation_dto.start_date}", status=status.HTTP_201_CREATED)

