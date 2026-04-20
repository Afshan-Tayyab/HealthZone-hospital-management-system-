from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentAPIView(APIView):
    """Get all appointments or create new appointment"""
    
    def get(self, request):
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AppointmentDetailAPIView(APIView):
    """Get, update or delete a single appointment"""
    
    def get(self, request, id):
        appointment = get_object_or_404(Appointment, id=id)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    
    def put(self, request, id):
        appointment = get_object_or_404(Appointment, id=id)
        serializer = AppointmentSerializer(appointment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        appointment = get_object_or_404(Appointment, id=id)
        appointment.delete()
        return Response({'message': 'Appointment deleted successfully'}, status=status.HTTP_204_NO_CONTENT)