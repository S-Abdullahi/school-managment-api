from random import choices
from tkinter import CASCADE
from django.db import models
import uuid
from rms_api.models import AuditableModel



STUDENT_SEX = (
    ('MALE','MALE'),
    ('FEMALE','FEMALE')
)

CLASS_LEVEL = (
    ('CRECHE','CRECHE'),
    ('NURSERY','NURSERY'),
    ('PRIMARY','PRIMARY'),
    ('JUNIOR SECONDARY','JUNIOR SECONDARY'),
    ('SENIOR SECONDARY','SENIOR SECONDARY')
)

TITLE = (
    ('MR','MR'),
    ('MRS','MRS')
)

        
# Create your models here.    
class Parent(AuditableModel):
    title = models.CharField(max_length=255, choices=TITLE, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    occupation = models.CharField(max_length=255, blank=True)
    parent_phone = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} {self.first_name}"

class Student(AuditableModel):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    middle_name = models.CharField(max_length=255, blank=True)
    sex = models.CharField(max_length=10, choices=STUDENT_SEX, default="MALE")
    level = models.CharField(max_length=255, blank=True, choices=CLASS_LEVEL)
    birthday = models.DateField(null=True,blank=True)
    Birthplace = models.CharField(max_length=255, blank=True)
    home_address = models.TextField(max_length=255, blank=True)
    parent = models.ForeignKey(Parent,on_delete= models.CASCADE, null=True, blank=True)
    

    def __str__(self):
        return f"{self.first_name} | {self.last_name} | {self.level}"
    

    

