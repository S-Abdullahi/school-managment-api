from argparse import Action
from django.shortcuts import render
from .serializer import StudentSerializer, ParentSerializer
from .models import Student, Parent
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    @action(detail=True, methods=['POST'])
    def register_student(self,request,serializer):
        student = self.serializer_class(data=request.data)
        try:
            if student.is_valid():
                student.save()
                return Response({'message': 'student successfully created'}, status=status.HTTP_201_CREATED)
        except:
            return Response({'message': 'student registration failed'}, status=status.HTTP_400_BAD_REQUEST)
        
    @action(detail=False, methods=['GET'])
    def student_summary(self,request,pk=None, **kwargs):
        qs = Student.objects.all()
        qs_creche = Student.objects.filter(level='CRECHE')
        qs_nursery = Student.objects.filter(level='NURSERY')
        qs_primary = Student.objects.filter(level='PRIMARY')
        qs_junior_secondary = Student.objects.filter(level='JUNIOR SECONDARY')
        qs_senior_secondary = Student.objects.filter(level="SENIOR SECONDARY")
        total_students = qs.count()
        total_creche = qs_creche.count()
        total_nursery = qs_nursery.count()
        total_primary = qs_primary.count()
        total_junior_secondary = qs_junior_secondary.count()
        total_senior_secondary = qs_senior_secondary.count()
        
        return Response({'total_students': total_students,
                         'total_creche': total_creche,
                         'total_nursery': total_nursery,
                         'total_primary': total_primary,
                         'total_junior_secondary': total_junior_secondary,
                         'total_senior_secondary': total_senior_secondary
                         }, status=status.HTTP_200_OK)
        
        

class ParentViewset(viewsets.ModelViewSet):
    queryset = Parent.objects.all()
    serializer_class = ParentSerializer
    
    def create(self,request):
        serializer = ParentSerializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response({"data":serializer.data, "status": "parent created successfully"},  status = status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors)
        except Exception as e:
            return Response({'message': str(e)})
        

        