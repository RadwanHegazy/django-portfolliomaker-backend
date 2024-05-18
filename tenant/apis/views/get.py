from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers import SiteTenant, TenantSerializer

class tenant_view (APIView) : 
    def get(self,request,tenant_name) : 
        try : 
            tenant = SiteTenant.objects.get(name=tenant_name)
            data = tenant.user.serializer(request.get_host())
        except SiteTenant.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        return Response(data,status=status.HTTP_200_OK)

class get_all_tenants (APIView) : 
    def get(self,request) : 
        data = SiteTenant.objects.all()
        serializer = TenantSerializer(data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)