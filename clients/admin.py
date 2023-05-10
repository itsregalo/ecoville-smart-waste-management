from django.contrib import admin
from .models import Client

# Register your models here.
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('user', 'address', 'city', 'points')
    list_filter = ('city', 'points')
    search_fields = ('user__email', 'address', 'city')
    ordering = ('user__email',)