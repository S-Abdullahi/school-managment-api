from django.shortcuts import render
from .models import User
from .serializer import CreateUserSerializer
from rest_framework import viewsets
# Create your views here.


class UsersViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    
    


