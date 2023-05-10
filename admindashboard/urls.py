from .views import *
from django.urls import path

app_name = "admin_dashboard"

urlpatterns = [
    path('', dashboard, name='admin-dashboard'),
]