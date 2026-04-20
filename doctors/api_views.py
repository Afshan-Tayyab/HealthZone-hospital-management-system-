from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorAPIView(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        return Response(serializer.data)