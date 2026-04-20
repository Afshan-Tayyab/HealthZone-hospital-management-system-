from django.urls import path
from .api_views import DoctorAPIView

urlpatterns = [
    path('', DoctorAPIView.as_view()),
]