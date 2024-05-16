from django.contrib import admin
from .models import SiteTenant

@admin.register(SiteTenant)
class TenantPanel (admin.ModelAdmin) : 
    list_display = ('user','name','is_working',)