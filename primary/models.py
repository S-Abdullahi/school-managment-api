from random import choices
from tkinter import CASCADE
from django.db import models
import uuid
from rms_api.models import AuditableModel
from parent.models import Parent



STUDENT_SEX = (
    ('MALE','MALE'),
    ('FEMALE','FEMALE')
)

SCHOOL_TYPE = (
    ('BASIC PRIMARY', 'BASIC PRIMARY'),
    ('SECONDARY','SECONDARY'),
)

CLASS_PRIMARY = (
    ('CRECHE','CRECHE'),
    ('NURSERY','NURSERY'),
    ('PRIMARY','PRIMARY'),
)

CLASS_SECONDARY = (
    ('JUNIOR SECONDARY', 'JUNIOR SECONDARY'),
    ('SENIOR SECONDARY', 'SENIOR SECONDARY'),
)

# Create your models here.    
    
class PrimaryStudent(AuditableModel):
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    middle_name = models.CharField(max_length=255, blank=True)
    level = models.CharField(max_length=255, blank=True, null=True, choices=CLASS_PRIMARY)
    sex = models.CharField(max_length=10, choices=STUDENT_SEX, default="MALE")
    birthday = models.DateField(null=True,blank=True)
    Birthplace = models.CharField(max_length=255, blank=True)
    home_address = models.TextField(max_length=255, blank=True)
    parent = models.ForeignKey(Parent,on_delete= models.CASCADE, null=True, blank=True)
    

    def __str__(self):
        return f"{self.first_name} | {self.last_name} | {self.level}"

