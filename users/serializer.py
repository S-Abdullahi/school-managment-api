import email
from rest_framework import serializers
from .models import User


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email','first_name','last_name','password','phone']
        extra_kwargs = {
            "password": {
                "write_only": True,
                'allow_blank': False,
                'allow_null': True,
                'min_length': 4
            }
        }
        
    def validate(self, data):
        password = data['password']
        email = data['email']
        
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('email already exist')
        if len(password) < 4:
            raise serializers.ValidationError('password too short')
        if User.objects.filter(password=password).exists():
            raise serializers.ValidationError('phone number already exist')
        return super().validate(data)
    
    def create(self, validated_data):
        return super().create(validated_data)