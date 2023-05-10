from django.contrib import admin
from .models import *

# Register your models here.



@admin.register(GarbageBin)
class GarbageBinAdmin(admin.ModelAdmin):
    list_display = ('location', 'capacity', 'bin_type', 'user')
    list_filter = ('bin_type', 'user')
    search_fields = ('location',)
    ordering = ('location',)

@admin.register(GarbageCollection)
class GarbageCollectionAdmin(admin.ModelAdmin):
    list_display = ('bin', 'pickup_time', 'status')
    list_filter = ('status',)
    search_fields = ('bin__location',)
    ordering = ('pickup_time',)

@admin.register(GarbageCollectionRequest)
class GarbageCollectionRequestAdmin(admin.ModelAdmin):
    list_display = ('user', 'bin', 'pickup_time', 'is_picked')
    list_filter = ('is_picked',)
    search_fields = ('bin__location',)
    ordering = ('pickup_time',)

@admin.register(WasteDisposal)
class WasteDisposalAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'waste_type')
    list_filter = ('waste_type',)
    search_fields = ('user__email',)
    ordering = ('user__email',)

@admin.register(CreditScore)
class CreditScoreAdmin(admin.ModelAdmin):
    list_display = ('user', 'score')
    search_fields = ('user__email',)
    ordering = ('user__email',)

@admin.register(Reward)
class RewardAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'cost')
    search_fields = ('user__email',)
    ordering = ('user__email',)

    