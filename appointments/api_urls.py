from django.urls import path
from .api_views import AppointmentAPIView, AppointmentDetailAPIView

urlpatterns = [
    path('', AppointmentAPIView.as_view(), name='appointment-list'),
    path('<int:id>/', AppointmentDetailAPIView.as_view(), name='appointment-detail'),
]