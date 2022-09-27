from xml.dom import ValidationErr
from rest_framework import serializers
from .models import Parent, Student



class StudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Student
        fields = '__all__'
        
    def validate(self, attrs):
        return super().validate(attrs)
        
class ParentSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    title = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    occupation = serializers.CharField()
    parent_phone = serializers.IntegerField()
    email = serializers.EmailField()
    
    def validate_parent_phone(self, value):
        if str(value).startswith('+234') and len(str(value)) != 14:
            raise serializers.ValidationError('Not a nigerian number')
        if len(str(value)) != 11:
            raise serializers.ValidationError('invalid phone number')
        if Parent.objects.filter(parent_phone=value).exists():
            raise serializers.ValidationError({'message':'Parent phone number already exists'})
        return value
    
    def validate_email(self, value):
        if Parent.objects.filter(email=value).exists():
            raise serializers.ValidationError({'message': 'email already exists'})
        return value
    
    def create(self, validated_data):
        return Parent.objects.create(**validated_data)