from rest_framework import serializers
from manager.models import User, Manager


class AdminRegisterationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['name', 'phone', 'address', 'password', 'password2']
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
        user.is_active = True
        user.save()
        manager = Manager.objects.create(
            user = user
        )
        return user


class LoginAdminSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=11)
    
    class Meta:
        model = User
        fields = ['phone', 'password']


class ManagerInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = ['national_code', 'bank_account_number']
    
    def create(self, validated_data):
        user = self.context['user'].id
        manager = Manager.objects.get(user=user)
        manager.national_code = validated_data['national_code']
        manager.bank_account_number = validated_data['bank_account_number']
        manager.save()
        return manager


class AdminPanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['id', 'password', 'is_active', 'is_admin', 'created_at', 'updated_at', 'last_login']


class AdminManagerPanelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        exclude = ['id']
        depth = 1

class AdminManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ['password', 'updated_at', 'is_active']


# ------------------------------------------------------------------------------
class SendPhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['phone', ]
    
    def validate(self, attrs):
        phone = attrs.get('phone')
        user = User.objects.filter(phone=phone).exists()
        if not user :
            raise serializers.ValidationError("phone number was not true!!")
        return attrs


class AdminResetPassword(serializers.ModelSerializer):
    password = serializers.CharField(max_length=255, 
                                     style = {'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(max_length=255, 
                                     style = {'input_type': 'password'}, write_only=True)
    class Meta:
        model = Manager
        fields = ['code', 'password', 'password2']
    
    def validate(self, attrs):
        user = self.context['user'].code
        code = attrs.get('code')
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if code != user :
            raise serializers.ValidationError("code was wrong!!")
        elif password != password2:
            raise serializers.ValidationError("password and confirm password dosen't match!!")
        return attrs


class AdminChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(max_length=255, 
                                     style = {'input_type': 'password'}, write_only=True)
    password2 = serializers.CharField(max_length=255, 
                                     style = {'input_type': 'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['password', 'password2']
    
    def validate(self, attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')
        if password != password2:
            raise Serializer.VlidationError("password and confirm password doesn't match!!")
        return attrs
