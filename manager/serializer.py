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
