from django.shortcuts import render
from accounts.models import User

# Create your views here.

def client_dashboard(request):
    return render(request, 'clients/client_dashboard.html')