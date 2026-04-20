from django.shortcuts import render, redirect, get_object_or_404
from .models import Doctor
from django.contrib.auth.decorators import login_required
from django.contrib import messages


@login_required
def doctors_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctors/doc_list.html', {'doctors': doctors})


@login_required
def add_doctor(request):
    if request.method == 'POST':
        doctor = Doctor(
            name=request.POST.get('name'),
            specialty=request.POST.get('specialty'),
            phone=request.POST.get('phone'),
            email=request.POST.get('email'),
            availability=request.POST.get('availability'),
        )
        doctor.save()
        messages.success(request, 'Doctor added successfully!')
        return redirect('/doctors/')
    return render(request, 'doctors/doc_add.html')


@login_required
def edit_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)
    return render(request, 'doctors/doc_edit.html', {'doctor': doctor})


@login_required
def update_doctor(request, id):
    if request.method == 'POST':
        doctor = get_object_or_404(Doctor, id=id)
        doctor.name = request.POST.get('name')
        doctor.specialty = request.POST.get('specialty')
        doctor.phone = request.POST.get('phone')
        doctor.email = request.POST.get('email')
        doctor.save()
        messages.success(request, 'Doctor updated successfully!')
    return redirect('/doctors/')


@login_required
def delete_doctor(request, id):
    doctor = get_object_or_404(Doctor, id=id)

    if request.method == 'POST':
        doctor.delete()
        messages.success(request, 'Doctor deleted successfully!')
        return redirect('/doctors/')

    # THIS LINE FIXES EVERYTHING
    return render(request, 'doctors/doc_delete.html', {'doctor': doctor})