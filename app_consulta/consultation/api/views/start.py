import logging

from django.core.exceptions import ValidationError
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api.dto.start_consultation_parameter_dto import StartConsultationParameterDto
from api.exceptions.invalid_data import InvalidDataException
from api.exceptions.invalid_operation import InvalidOperationException
from api.service.start_consultation_service import StartConsultationService


class StartConsutationView(APIView):
    """ View para início de uma consulta
        url: /app/consultation/start/ """

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Definição para autenticação
        self.authentication_classes = [SessionAuthentication, BasicAuthentication]
        self.permission_classes = [IsAuthenticated]

        # Classe de serviço para inicio da consulta
        self.start = StartConsultationService()

    def post(self, request):
        logging.info(f"API consultation.start acessada por {request.user.username}")

        try:
            # Converte a entrada em DTO
            input_dto = StartConsultationParameterDto().from_dict(JSONParser().parse(request)).validate()
            # Chama o serviço para iniciar a consulta
            consultation_dto = self.start.begin(input_dto)

        except (InvalidDataException, ValidationError, InvalidOperationException) as e:
            # Responde com o status 400 no caso de existir dados inválidos no parametro
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            # Responde com status 400 e registra em log no caso de ocorrer um erro não especificado
            logging.exception("Ocorreu uma operação inválida ao iniciar a consulta.")
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

        return JsonResponse(consultation_dto.__dict__, status=status.HTTP_201_CREATED)

