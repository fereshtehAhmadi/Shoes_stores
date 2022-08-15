from rest_framework import serializers
from accounts.models import Accounts, Validation


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Validation
        fields = ['phone', ]


class CodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Validation
        fields = ['code', ]
    
    def validate(self, attrs):
        valid = self.context['valid'].code
        code = attrs.get('code')
        if code != valid :
            raise serializers.ValidationError("code was wrong!!")
        return attrs


class UserRegisterationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ['username', 'name','password', ]
        extra_kwargs={
            'password':{'write_only': True}
        }
    
    def create(self, validated_data):
        phone = self.context['valid'].phone
        user = User.objects.create(**validated_data)
        user.phone = phone
        return user
