from django.shortcuts import render, redirect
from .forms import AppointmentForm
from .models import Appointment

def book_appointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.patient = request.user
            obj.save()
            return redirect(f'/appointments/appointments/{request.user.id}')
    else:
        form = AppointmentForm()
    return render(request, 'book_appointment.html', {'form': form})

def appointments(request, **kwargs):
    if id_:= kwargs.pop('id', None):
        appointments = Appointment.objects.filter(patient__id=id_)
    else:
        appointments = Appointment.objects.all()
    return render(request, 'appointments.html', {'appointments': appointments})

def approve_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.reject = False
    appointment.approved = True
    appointment.save()
    return redirect(f'/appointments/appointments/{appointment.patient.id}')

def reject_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.approved = False
    appointment.reject = True
    appointment.save()
    return redirect(f'/appointments/appointments/{appointment.patient.id}')

def delete_appointment(request, appointment_id):
    appointment = Appointment.objects.get(id=appointment_id)
    appointment.delete()
    return redirect('appointments:appointments')
