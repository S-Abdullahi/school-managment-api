from rest_framework import serializers
from .models import Teachers


class Teacherserializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = Teachers
        exclude = ['pasword']
        