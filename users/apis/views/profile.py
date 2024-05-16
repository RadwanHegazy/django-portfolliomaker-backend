from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.response import Response
from users.models import User

class profile_view (APIView) :
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, **kwargs) : 
        user:User = request.user
        data = user.serializer(host=request.get_host())
        return Response(data,status=status.HTTP_200_OK)