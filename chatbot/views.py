from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home(request):
    return render(request, 'chatbot/home.html')

@login_required
def medical_history(request):
    return render(request, 'chatbot/medical_history.html')

