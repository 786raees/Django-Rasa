from django.urls import path
from . import views as users_views

app_name = "users"

urlpatterns = [
    path('patients/', users_views.patient_list, name='patient_list'),
]
