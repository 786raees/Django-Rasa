from django.urls import path
from . import views

app_name="appointments"

urlpatterns = [
    path('appointments/', views.appointments, name='appointments'),
    path('appointments/<int:id>/', views.appointments, name='appointments'),
    path('appointments/new/', views.book_appointment, name='book_appointment'),
    path('appointments/<int:appointment_id>/approve/', views.approve_appointment, name='approve_appointment'),
    path('appointments/<int:appointment_id>/reject/', views.reject_appointment, name='reject_appointment'),
    path('appointments/<int:appointment_id>/delete/', views.delete_appointment, name='delete_appointment'),

]
