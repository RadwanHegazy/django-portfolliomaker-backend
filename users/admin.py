from django.contrib import admin
from .models import User, Site


@admin.register(User)
class UserPanel (admin.ModelAdmin) : 
    list_display = ('full_name','email',)
    
@admin.register(Site)
class UserPanel (admin.ModelAdmin) : 
    list_display = ('name','is_working',)
