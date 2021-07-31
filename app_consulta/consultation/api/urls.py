from django.urls import path

from api.views.finish import FinishConsutationView
from api.views.start import StartConsutationView

urlpatterns = [
    path("consultation/start/", StartConsutationView.as_view(), name="start_consultation"),
    path("consultation/finish/", FinishConsutationView.as_view(), name="finish_consultation"),
]