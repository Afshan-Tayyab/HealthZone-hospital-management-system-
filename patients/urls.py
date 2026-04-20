from django.urls import path
from . import views  # Add this import

urlpatterns = [
    path('', views.patients_list, name='patients_list'),
    path('add/', views.add_patient, name='add_patient'),
    path('edit/', views.edit_patient, name='edit_patient'),
    path('update/', views.update_patient, name='update_patient'),
    path('delete/', views.delete_patient, name='delete_patient'),
]