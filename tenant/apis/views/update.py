from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import UpdateTenantSerializer, SiteTenant

class update_view(APIView) : 
    serializer_class = UpdateTenantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, **kwargs) : 
        if not request.has_tenant :
            return Response(status=status.HTTP_400_BAD_REQUEST)

        tenant:SiteTenant = request.tenant
        
        if tenant.user != request.user : 
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        serializer = self.serializer_class(tenant,data=request.data)
        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
