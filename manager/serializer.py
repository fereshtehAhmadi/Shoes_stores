from rest_framework import serializers
from manager.models import User

class AdminRegisterationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'name', 'phone', 'address', 'national_code', 'bank_account_number', 'password', 'password2']
        extra_kwargs={
            'password':{'write_only': True}
        }
    
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2 :
            raise serializers.ValidationError("password and confirm password dosen't match!!")
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')
        user = User.objects.create(**validated_data, is_active=True)
        user.set_password(validated_data['password'])
        user.save()
        return user


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
