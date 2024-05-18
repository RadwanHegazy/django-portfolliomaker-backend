from ..models import SiteTenant
from rest_framework import serializers

class TenantSerializer (serializers.ModelSerializer) : 
    class Meta:
        model = SiteTenant
        fields = ('name','user',)

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = {
            'full_name' : instance.user.full_name,
            'picture' : instance.user.picture.url,
        }
        return data

class UpdateTenantSerializer (serializers.ModelSerializer) : 
    name = serializers.CharField(read_only=True)
    class Meta:
        model = SiteTenant
        fields = ('name','about','is_working','jop_title',)
