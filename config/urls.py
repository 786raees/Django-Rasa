from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('appointments/', include('appointments.urls')),
    path('', include('users.urls')),
    path('', include('chatbot.urls')),
    path('__debug__/', include('debug_toolbar.urls')),

]
