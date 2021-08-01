import logging

from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.converter.consultation_converter import ConsultationConverter
from api.exceptions.invalid_data import InvalidDataException
from api.exceptions.invalid_operation import InvalidOperationException
from api.service.start_consultation_service import StartConsultationService


class StartConsutationView(APIView):
    """ View para início de uma consulta
        url: /app/consultation/start/ """

    # Definição para autenticação
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    # Classe de serviço para inicio da consulta
    start = StartConsultationService()

    # Conversor da entrada em dto
    converter = ConsultationConverter()

    def post(self, request):
        logging.info(f"API consultation.start acessada por {request.user.username}")

        try:
            # Converte o texto de entrada em dto
            input_dto = self.converter.start_data_from_text(request.body)
            # Chama o serviço para iniciar a consulta
            consultation_dto = self.start.begin(input_dto)

        except InvalidDataException as e:
            # Responde com o status 400 no caso de existir dados inválidos no parametro
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        except InvalidOperationException as e:
            # Responde com status 400 no caso de ocorrer um erro no serviço
            logging.exception("Ocorreu uma operação inválida ao iniciar a consulta.")
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        return Response(self.converter.dto_to_json(consultation_dto), status=status.HTTP_201_CREATED)

