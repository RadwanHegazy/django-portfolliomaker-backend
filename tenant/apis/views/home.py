from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from ...models import SiteTenant
from ..serializers import TenantSerializer

class home_view(APIView) : 

    def get(self, request, **kwargs) :
         
        if request.has_tenant :
            data = self.tenant_on(request.tenant,request.get_host())
        else:
            data = self.tenant_off()

        return Response(data,status=status.HTTP_200_OK)
    
    def tenant_on(self, tenant:SiteTenant,host) -> dict:
        user_of_tenant = tenant.user
        return user_of_tenant.serializer(host)
    

    def tenant_off (self) -> dict:
        serializer = TenantSerializer(
            SiteTenant.objects.all(),many=True
        )

        return serializer.data