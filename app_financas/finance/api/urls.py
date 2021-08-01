from django.urls import path

from api.views.record import RecordView

urlpatterns = [
    path("finance/record/", RecordView.as_view(), name="record"),
]

