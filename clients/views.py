from django.shortcuts import render
from accounts.models import User
from .models import Client
from admindashboard.models import *

# Create your views here.

def client_dashboard(request):
    try:
        user_credit_score = CreditScore.objects.get(user=request.user).score
    except CreditScore.DoesNotExist:
        user_credit_score = CreditScore.objects.create(user=request.user, score=0)
    user_garbage_bins = GarbageBin.objects.filter(user=request.user)
    user_garbage_collections = GarbageCollection.objects.filter(bin__in=user_garbage_bins).count()
    user_garbage_collection_requests = GarbageCollectionRequest.objects.filter(user=request.user).filter(is_picked=False).count()

    context = {
        'user_credit_score': user_credit_score,
        'user_garbage_bins': user_garbage_bins,
        'user_garbage_collections': user_garbage_collections,
        'pending_user_garbage_collection_requests': user_garbage_collection_requests
    }

    return render(request, 'clients/client_dashboard.html', context)