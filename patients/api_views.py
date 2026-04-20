from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Patient
from .serializers import PatientSerializer

class PatientAPIView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)