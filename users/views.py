from django.shortcuts import render
from django.http import HttpResponse
from .models import SiteTenant

def home (request) :
    has_tenant:bool = request.has_tenant

    if has_tenant : 
        tenant:SiteTenant = request.tenant
        return HttpResponse(tenant.name)
    else:
        pass
        
    return HttpResponse('Done')