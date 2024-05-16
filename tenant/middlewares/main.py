
from users.models import SiteTenant
from django.http import Http404

class TenantMiddleware:
    def __init__(self, get_response) -> None:
        self.get_response = get_response

    def __call__(self,request) :
        hostname = request.get_host()
        request.has_tenant = False
        
        if len(str(hostname).split('.')) > 1 :
            tenant_name =  str(hostname).split('.')[0]
            try : 
                site = SiteTenant.objects.get(name=tenant_name,is_working=True)
                request.has_tenant = True
                request.tenant = site
            except SiteTenant.DoesNotExist:
                raise Http404(request)

        response = self.get_response(request)
        return response