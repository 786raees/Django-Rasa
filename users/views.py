from django.shortcuts import render
from .models import AllUser

def patient_list(request):
    patients = AllUser.objects.exclude(user_type="doctor")
    return render(request, 'users/patient_list.html', {'patients': patients})
