from django.urls import path

from endpoint.views.iniciar import IniciarConsulta

urlpatterns = [
    path("consulta/iniciar/", IniciarConsulta.as_view(), name="iniciar_consulta"),

]