from rest_framework import serializers
from .models import Parent


class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parent
        fields = '__all__'
        
    def validate(self, data):
        phone = data['parent_phone']
        email = data['email']
        if len(phone) < 11:
            raise serializers.ValidationError('phone number not valid')
        if phone.startswith('+') and len(phone) != 14:
            raise serializers.ValidationError('phone number not valid')
        if Parent.objects.filter(parent_phone=phone).exists():
            raise serializers.ValidationError('phone already exist')
        if Parent.objects.filter(email=email).exists():
            raise serializers.ValidationError('email already exist')
        return data
    
    def create(self, validated_data):
        return Parent.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
            
