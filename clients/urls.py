from django.urls import path
from .views import *

app_name = "clients"

urlpatterns = [
    path('', client_dashboard, name='client-dashboard'),
]