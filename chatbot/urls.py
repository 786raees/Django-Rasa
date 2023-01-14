from django.urls import path
from . import views as chatbot_views

app_name = "chatbot"

urlpatterns = [
    path("", chatbot_views.home, name="home")
]
