from multiprocessing import context
from urllib import response
from django.shortcuts import render
from rest_framework.response import Response
from uritemplate import partial
from .serializer import ParentSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from .models import Parent

# Create your views here.
class ParentViewset(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    
    def create(self,request):
        try:
            serializer = ParentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': True, 'data': serializer.data, 'message': 'parent created successfully'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'sucess': False}, status=status.HTTP_400_BAD_REQUEST,)
        except Exception as e:
            return Response({'message': str(e)})
        
    def retrieve(self, request,pk=None):
        try:
            parent = Parent.objects.get(pk=pk)
            serializer = self.serializer_class(parent)
            if not parent:
                return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'success': True, 'data':serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'success':False,'message': 'Parent with ID does not exist'}, status=status.HTTP_400_BAD_REQUEST)  
        
    def partial_update(self, request, pk=None):
        try:
            parent_data = Parent.objects.get(pk=pk)
            if not parent_data:
                return Response({'success': False}, status=status.HTTP_400_BAD_REQUEST)
            serializer = ParentSerializer(instance=parent_data, data=request.data, context={'request':request}, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': True, 'data': serializer.data, 'message': 'parent data updated successfully'}, status=status.HTTP_200_OK)
            return Response({'sucess': False, 'data': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    @action (detail=False, methods=['GET'])
    def parent_summary(self, request):
        try:
            parent = Parent.objects.all()
            parent_number = parent.count()
            return Response({'success': True, 'total_parent': parent_number}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'success': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        