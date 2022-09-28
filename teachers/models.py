from enum import unique
from secrets import choice
from django.db import models
from rms_api.models import AuditableModel

SEX = (
    ('MALE', 'MALE'),
    ('FEMALE','FEMALE')
)

RELIGION = (
    ('ISLAM', 'ISLAM'),
    ('CHRISTIANITY', 'CHRISTIANITY')
)

CLASS_LEVEL = (
    ('CRECHE','CRECHE'),
    ('NURSERY','NURSERY'),
    ('PRIMARY','PRIMARY'),
    ('JUNIOR SECONDARY','JUNIOR SECONDARY'),
    ('SENIOR SECONDARY','SENIOR SECONDARY')
)

EDUCATION = (
    ('COLLEGE OF EDUCATION','COLLEGE OF EDUCATION'),
    ('UNIVERSITY','UNIVERSITY')
)

SUBJECT = (
    ('MATHEMATICS', 'MATHEMATICS'),
    ('ENGLISH LANGUAGE', 'ENGLISH LANGUAGE'),
    ('PHYSICS', 'PHYSICS'),
    ('CHEMISTRY','CHEMISTRY'),
    ('BIOLOGY','BIOLOGY'),
    ('ECONOMICS','ECONOMICS')
)

# Create your models here.
class Teachers(AuditableModel):
    name = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=False)
    sex = models.CharField(max_length=255, choices=SEX, default="MALE")
    address = models.TextField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=14, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True, unique=True)
    birthday = models.DateField(null=True, blank=True)
    religion = models.CharField(max_length=255, blank=True, null=True, choices=RELIGION)
    classlevel = models.CharField(max_length=255, blank=True, null=True, choices=CLASS_LEVEL)
    education_background = models.CharField(max_length=255, blank=True, null=True, choices=EDUCATION)
    institution_name = models.CharField(max_length=255, blank=True, null=True)
    special_skills = models.CharField(max_length=255, blank=True, null=True)
    
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return f"{self.name} | {self.classlevel}"
    