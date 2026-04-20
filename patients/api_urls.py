from django.urls import path
from .api_views import PatientAPIView

urlpatterns = [
    path('', PatientAPIView.as_view()),
]