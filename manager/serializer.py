from rest_framework import serializers
from manager.models import User


class AdminRegisterationSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model = User
        fields = ['username', 'name', 'phone', 'phone', 'address', 'national_code', 'bank_account_number', 'password', 'password2']
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
        return User.objects.create(**validated_data, is_staff=True)

