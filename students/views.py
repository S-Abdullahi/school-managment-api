from argparse import Action
from multiprocessing import context
from django.http import QueryDict
from django.shortcuts import render
from uritemplate import partial
from .serializer import ParentSerializer, PrimaryStudentSerializer, SecondaryStudentSerializer, SchoolSerializer
from .models import Student, Parent, PrimaryStudent, SecondaryStudent, School
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
import datetime

# Create your views here.
class SchoolViewset(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer
    
    def create(self, request):
        try:
            school = SchoolSerializer(data=request.data)
            if school.is_valid():
                school.save()
                return Response({'success': True, 'data': request.data, 'message': 'School created successfully'}, status=status.HTTP_201_CREATED)
            return Response(school.errors)
        except Exception as e:
            return Response({'message': str(e)})

class PrimaryStudentViewset(viewsets.ModelViewSet):
    queryset = PrimaryStudent.objects.all()
    serializer_class = PrimaryStudentSerializer
            
    def create(self, request):
        try:
            serializer = PrimaryStudentSerializer(data=request.data)
            if serializer.is_valid(): 
                serializer.save()
                return Response({'sucess': True, "data": serializer.data, 'message': 'Primary school student created successfully'}, status=status.HTTP_201_CREATED)
            return Response({'sucess': False}, status=status.HTTP_400_BAD_REQUEST)
    
        except Exception as e:
            return Response({'message': str(e)})
    @action(detail=False, methods=['GET'])
    def student_primary(self, request, pk=None, **kwargs):
        qs = Student.objects.filter()
        
    @action(detail=False, methods=['GET'])
    def primary_student_summary(self,request,pk=None, **kwargs):
        qs = PrimaryStudent.objects.all()
        qs_creche = PrimaryStudent.objects.filter(level='CRECHE')
        qs_nursery = PrimaryStudent.objects.filter(level='NURSERY')
        qs_primary = PrimaryStudent.objects.filter(level='PRIMARY')
        # qs_junior_secondary = PrimaryStudent.objects.filter(level='JUNIOR SECONDARY')
        # qs_senior_secondary = PrimaryStudent.objects.filter(level="SENIOR SECONDARY")
        total_students = qs.count()
        total_creche = qs_creche.count()
        total_nursery = qs_nursery.count()
        total_primary = qs_primary.count()
        # total_junior_secondary = qs_junior_secondary.count()
        # total_senior_secondary = qs_senior_secondary.count()
        
        return Response({'total_students': total_students,
                         'total_creche': total_creche,
                         'total_nursery': total_nursery,
                         'total_primary': total_primary
                        #  'total_junior_secondary': total_junior_secondary,
                        #  'total_senior_secondary': total_senior_secondary
                         }, status=status.HTTP_200_OK)
        
    @action(detail=False, methods=['GET'])
    def student_gender_summary(self, request, pk=None, **kwargs):
        qs_male = Student.objects.filter(sex='MALE')
        qs_female = Student.objects.filter(sex='FEMALE')
        
        total_male = qs_male.count()
        total_female = qs_female.count()
        return Response(
            {'success': True, 
             "total_male": total_male,
             "total_female": total_female}, status=status.HTTP_200_OK
        )
        
class SecondaryStudentViewset(viewsets.ModelViewSet):
    queryset = SecondaryStudent.objects.all()
    serializer_class = SecondaryStudentSerializer
    
    @action(detail=False, methods=['GET'])
    def secondary_students_summary(self,request, pk=None, **kwargs):
        qs = self.get_queryset()
        total_secondary_students = qs.count()
        return Response(
            {'success': True,
             'total_secondary_students': total_secondary_students}, 
            status = status.HTTP_200_OK
        )
        
class ParentViewset(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    
    def create(self,request):
        try:
            serializer = ParentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data, "status": "parent created successfully"},  status = status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors)
        except Exception as e:
            return Response({'message': str(e)})
    
    def partial_update(self, request,pk):
        try:
            parent_data = self.get_queryset().filter(pk=pk).first()
            if not parent_data:
                return Response(
                    {'success': False, 'message': 'Parent data does not exist'},
                    status = status.HTTP_400_BAD_REQUEST,
                )
            serializer = ParentSerializer(instance=parent_data, data=request.data, context={'request':request}, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response({'success': True,
                                 'message':'parent updated successfully',
                                 'data': serializer.data},
                                status = status.HTTP_200_OK)
            return Response(
                {'sucess': False, 'message': serializer.errors}
            )
        except Exception as e:
            return Response({'message': str(e)})
            
      
        
    
    @action(detail=False, methods=['GET'])
    def parent_summary(self, request, pk=None, **kwargs):
        qs = Parent.objects.all()
        total_parent = qs.count()
        return Response({'success':True, 
                         'Total parent': total_parent}, status=status.HTTP_200_OK)
        

        