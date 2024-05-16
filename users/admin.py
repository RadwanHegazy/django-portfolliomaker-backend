from django.contrib import admin
from .models import User


@admin.register(User)
class UserPanel (admin.ModelAdmin) : 
    list_display = ('full_name','email',)
