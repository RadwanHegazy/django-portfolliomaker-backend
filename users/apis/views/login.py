from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from ..serializers import LoginSerializer

class login_view (APIView) : 
    serializer_class = LoginSerializer

    def post(self,request,**kwargs) : 
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid() : 
            return Response(serializer.tokens,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        