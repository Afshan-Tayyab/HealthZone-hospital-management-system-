from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from patients.models import Patient
from doctors.models import Doctor

# Create your views here.
@login_required
def dashboard_home(request):
    context = {
        'patient_count': Patient.objects.count(),
        'doctor_count': Doctor.objects.count(),
    }
    return render(request, "dashboard_home.html", context)