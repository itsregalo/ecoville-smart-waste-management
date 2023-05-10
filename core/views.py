from django.shortcuts import render
from django.shortcuts import redirect
# import login_required
from django.contrib.auth.decorators import login_required



# Create your views here.

def index(request):
    return render(request, 'index.html')


@login_required(login_url='accounts:login')
def dashboard(request):
    if request.user.is_authenticated:
        if request.user.is_staff or request.user.is_superuser or request.user.is_admin:
            return redirect('admin_dashboard:admin-dashboard') # redirect to the admin dashboard
        else: # if the user is not an admin
            return redirect('clients:client-dashboard') # redirect to the client dashboard
    else: # if the user is not authenticated
        return render(request, 'index.html')