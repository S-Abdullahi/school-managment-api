from django.shortcuts import render
from rest_framework import viewsets
from .serializer import TeacherSerializer
from .models import Teachers
# Create your views here.

class TeacherViewset(viewsets.ModelViewSet):
    queryset = Teachers.objects.all()
    serializer_class = TeacherSerializer