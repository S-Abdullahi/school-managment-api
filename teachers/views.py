from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from .models import Teachers
from .serializers import Teacherserializer
# Create your views here.


class TeachersViewset(viewsets.ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = Teacherserializer
    
