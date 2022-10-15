from random import choices
from tabnanny import verbose
from django.db import models
from django.conf import settings

CLASS_LEVEL = (
    ('CRECHE', 'CRECHE'),
    ('PRIMARY','PRIMARY'),
    ('JUNIOR SECONDARY', 'JUNIOR SECONDARY'),
    ('SENIOR SECONDARY', 'SENIOR SECONDARY'),
)
QUALIFICATION = (
    ('NCE', 'NCE'),
    ('OND', 'OND'),
    ('HND', 'HND'),
    ('BSC', 'BSC'),
)

MARITAL_STATUS = (
    ('SINGLE', 'SINGLE'),
    ('ENGAGED', 'ENGAGED'),
    ('MARRIED', 'MARRIED'),
)

class Teachers(models.Model):
    teacher = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, related_name='teacher')
    class_level = models.CharField(max_length=255, choices=CLASS_LEVEL, blank=True, null=True)
    qualification = models.CharField(max_length=255, choices=QUALIFICATION, blank=True, null=True)
    marital_status = models.CharField(max_length=50, choices=MARITAL_STATUS, blank=True, null=True)
    address = models.TextField(max_length=255, blank=True, null=True)
    experience = models.TextField(max_length=255, blank=True, null=True)
    
    class Meta:
        verbose_name_plural = ('Teachers')
    
    def __str__(self):
        return f'{self.teacher.first_name} {self.teacher.last_name}' 
    
    