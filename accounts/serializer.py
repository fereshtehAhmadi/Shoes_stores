from rest_framework import serializers
from accounts.models import Accounts, Validation


class PhoneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Validation
        fields = ['phone', ]


# class CodeSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Validation
#         fields = ['code', ]
    
#     def validate(self, attrs):
#         valid = self.context['valid'].code
#         code = attrs.get('code')
#         if code != valid :
#             raise serializers.ValidationError("code was wrong!!")
#         return attrs


class UserRegisterationSerializer(serializers.ModelSerializer):
    code = serializers.CharField(write_only=True)
    phone = serializers.CharField(default='09190000000')
    class Meta:
        model = Accounts
        fields = ['code', 'name', 'phone', 'password', ]
        extra_kwargs={
            'password':{'write_only': True}
        }
    
    def validate(self, attrs):
        valid = self.context['valid'].code
        phone = self.context['valid'].phone
        code = attrs.get('code')
        if code != valid :
            raise serializers.ValidationError("code was wrong!!")
        if attrs.get('phone') == None:
            attrs['phone']=phone
        return attrs

    def create(self, validated_data):
        validated_data.pop('code')
        phone = self.context['valid'].phone
        user = Accounts.objects.create(**validated_data)
        user.phone = phone
        user.set_password(validated_data['password'])
        user.save()
        valid = Validation.objects.get(phone=phone)
        valid.delete()
        return user


class UserLoginSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=11)
    class Meta:
        model = Accounts
        fields = ['phone', 'password']
