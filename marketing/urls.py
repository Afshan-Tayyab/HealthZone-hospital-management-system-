from django.urls import path


from .views import marketing_home
  
urlpatterns = [
    path('', marketing_home),
  ]

