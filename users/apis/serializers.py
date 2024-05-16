from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import serializers
from ..models import User
from rest_framework.validators import ValidationError

class GetTokens :
    @property
    def tokens (self) -> dict: 
        # [NOTE] in main class you must init the user model in self.user variable
        user_token = RefreshToken.for_user(self.user)
        return {
            'token' : str(user_token.access_token)
        }

class LoginSerializer (serializers.Serializer, GetTokens) : 
    email = serializers.EmailField()
    password = serializers.CharField()

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']

        try :
            self.user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError({
                'message' : "invalid email"
            },code=400)
        
        if not self.user.check_password(password) : 
            raise ValidationError({
                'message' : "invalid password"
            },code=400)
        

        return attrs
    
class RegisterSerilaizer (serializers.ModelSerializer, GetTokens) : 
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('full_name','email','password','picture')

    def validate(self, attrs):
        email = attrs['email']

        if User.objects.filter(email=email).exists() : 
            raise ValidationError({
                'message' : 'user with email already exists'
            },code=400)
    
        return attrs
    
    def save(self, **kwargs):
        self.user = User.objects.create_user(**self.validated_data)
        return self.user
