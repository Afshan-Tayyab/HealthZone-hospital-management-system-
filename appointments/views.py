from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Appointment
from patients.models import Patient
from doctors.models import Doctor

@login_required
def appointment_list(request):
    appointments = Appointment.objects.all()
    patients = Patient.objects.all()
    doctors = Doctor.objects.all()
    context = {
        'appointments': appointments,
        'patients': patients,
        'doctors': doctors,
    }
    return render(request, 'appointments/app_list.html', context)

@login_required
def add_appointment(request):
    if request.method == 'POST':
        patient = get_object_or_404(Patient, id=request.POST.get('patient_id'))
        doctor = get_object_or_404(Doctor, id=request.POST.get('doctor_id'))
        
        appointment = Appointment(
            patient=patient,
            doctor=doctor,
            appointment_date=request.POST.get('appointment_date'),
            appointment_time=request.POST.get('appointment_time'),
            appointment_status=request.POST.get('appointment_status', 'Scheduled'),
            reason=request.POST.get('reason'),
        )
        appointment.save()
        messages.success(request, 'Appointment booked successfully!')
    return redirect('/appointments/')

@login_required
def update_appointment(request, id):
    if request.method == 'POST':
        appointment = get_object_or_404(Appointment, id=id)
        appointment.appointment_date = request.POST.get('appointment_date')
        appointment.appointment_time = request.POST.get('appointment_time')
        appointment.appointment_status = request.POST.get('appointment_status')
        appointment.reason = request.POST.get('reason')
        appointment.save()
        messages.success(request, 'Appointment updated successfully!')
    return redirect('/appointments/')

@login_required
def delete_appointment(request, id):
    if request.method == 'POST':
        appointment = get_object_or_404(Appointment, id=id)
        appointment.delete()
        messages.success(request, 'Appointment deleted successfully!')
    return redirect('/appointments/')
