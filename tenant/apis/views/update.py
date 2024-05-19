from rest_framework import status,permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import UpdateTenantSerializer, SiteTenant

class update_view(APIView) : 
    serializer_class = UpdateTenantSerializer
    permission_classes = [permissions.IsAuthenticated]

    def put(self, request, **kwargs) : 
        tenant:SiteTenant = SiteTenant.objects.get(user=request.user)
        
        serializer = self.serializer_class(tenant,data=request.data)
        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
