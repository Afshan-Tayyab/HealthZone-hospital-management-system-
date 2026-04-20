from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Patient

def patients_list(request):  # Changed from patients_list to patient_list
    patients = Patient.objects.all()
    return render(request, 'list.html', {'patients': patients})

def add_patient(request):
    if request.method == 'POST':
        patient = Patient(
            name=request.POST.get('name'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            age=request.POST.get('age'),
            gender=request.POST.get('gender'),
            address=request.POST.get('address')
        )
        patient.save()
        messages.success(request, f"Patient {patient.name} added successfully! 🏥")
    return redirect('/patients/')

def edit_patient(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        patient = Patient.objects.get(id=patient_id)
        patient.name = request.POST.get('name')
        patient.phone = request.POST.get('phone')
        patient.email = request.POST.get('email')
        patient.age = request.POST.get('age')
        patient.gender = request.POST.get('gender')
        patient.address = request.POST.get('address')
        patient.save()
        messages.success(request, f"Patient {patient.name} updated successfully! ✏️")
    return redirect('/patients/')

def update_patient(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        patient = Patient.objects.get(id=patient_id)
        patient.name = request.POST.get('name')
        patient.phone = request.POST.get('phone')
        patient.email = request.POST.get('email')
        patient.age = request.POST.get('age')
        patient.gender = request.POST.get('gender')
        patient.address = request.POST.get('address')
        patient.save()
        messages.success(request, f"Patient {patient.name} updated successfully! 🔄")
    return redirect('/patients/')

def delete_patient(request):
    if request.method == 'POST':
        patient_id = request.POST.get('patient_id')
        patient = Patient.objects.get(id=patient_id)
        patient_name = patient.name
        patient.delete()
        messages.success(request, f"Patient {patient_name} deleted successfully! 🗑️")
    return redirect('/patients/')
