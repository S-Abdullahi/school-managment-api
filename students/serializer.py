from xml.dom import ValidationErr
from rest_framework import serializers
from .models import Parent, Student, PrimaryStudent, SecondaryStudent, School
import datetime


# class StudentSerializer(serializers.ModelSerializer):
    
#     class Meta:
#         model = Student
#         fields = '__all__'
        
#     def validate(self, attrs):
#         return super().validate(attrs)
        
# class ParentsSerializer(serializers.Serializer):
#     id = serializers.UUIDField(read_only=True)
#     title = serializers.CharField()
#     first_name = serializers.CharField()
#     last_name = serializers.CharField()
#     occupation = serializers.CharField()
#     parent_phone = serializers.CharField()
#     email = serializers.EmailField()
    
#     def validate_parent_phone(self, value):
#         if str(value).startswith('+234') and len(str(value)) != 14:
#             raise serializers.ValidationError('Not a nigerian number')
#         if len(str(value)) != 11:
#             raise serializers.ValidationError('invalid phone number')
#         if Parent.objects.filter(parent_phone=value).exists():
#             raise serializers.ValidationError({'message':'Parent phone number already exists'})
#         return value
    
#     def validate_email(self, value):
#         if Parent.objects.filter(email=value).exists():
#             raise serializers.ValidationError({'message': 'email already exists'})
#         return value
    
#     def create(self, validated_data):
#         return Parent.objects.create(**validated_data)
    

class PrimaryStudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = PrimaryStudent
        fields = '__all__'
        
    # def validate(self, data):
    #     dob = data['birthday']
    #     level = data['level']
    #     print(dob, 'rrr')
    #     year = datetime.datetime.date()
    #     print(year, 'yyyy')
    #     if year < 5 and level == 'PRIMARY':
    #         raise serializers.ValidationError('student age is not eligible for this class')
    #     return super().validate(data)
        
class SecondaryStudentSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = SecondaryStudent
        fields = '__all__'
        
class SchoolSerializer(serializers.ModelSerializer):
     
    class Meta:
        model = School
        fields = '__all__'

