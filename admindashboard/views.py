from django.shortcuts import render
from accounts.models import User
from clients.models import Client
from admindashboard.models import (
    GarbageBin, GarbageCollection, GarbageCollectionRequest,
    WasteDisposal, CreditScore, Reward
)

# Create your views here.


def dashboard(request):
    total_clients = Client.objects.all().count()
    total_users = User.objects.all().count()
    total_bins = GarbageBin.objects.all().count()
    latest_requests = GarbageCollectionRequest.objects.all().order_by('-id')[:10]
    total_requests = GarbageCollectionRequest.objects.all().count()
    total_disposals = WasteDisposal.objects.all().count()
    total_pending_request = GarbageCollectionRequest.objects.filter(is_picked=False).count()
    pending_collections = GarbageCollectionRequest.objects.filter(is_picked=False)
    scores_leaderboard = CreditScore.objects.all().order_by('-score')[:10]
    context = {
        'total_clients': total_clients,
        'total_bins': total_bins,
        'total_collections': GarbageCollectionRequest.objects.filter(is_picked=True).count(),
        'total_requests': total_requests,
        'total_disposals': total_disposals,
        'total_users': total_users,
        'total_pending_request': total_pending_request,
        'pending_collections':pending_collections,
        'latest_requests': latest_requests,
        'scores_leaderboard': scores_leaderboard,

    }
    return render(request, 'admin-dashboard/admin-dashboard.html', context)