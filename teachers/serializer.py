from rest_framework import serializers
from .models import Teachers
from users.serializer import CreateUserSerializer

class TeacherSerializer(serializers.ModelSerializer):
    teacher = CreateUserSerializer(read_only=True)
    class Meta:
        model = Teachers
        fields = '__all__'
        
    def create(self, validated_data):
        return super().create(validated_data)

