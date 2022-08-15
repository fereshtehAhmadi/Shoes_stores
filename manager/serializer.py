from rest_framework import serializers
from manager.models import User

class AdminRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'name', 'phone', 'address', 'national_code', 'bank_account_number', 'password']
        extra_kwargs={
            'password':{'write_only': True}
        }
    
    
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginAdminSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=200)
    class Meta:
        model = User
        fields = ['username', 'password']


class AdminPanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['id', 'password', 'is_active', 'is_admin', 'is_staff', 'created_at', 'updated_at', 'last_login']


class AdminManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'updated_at', 'is_active']