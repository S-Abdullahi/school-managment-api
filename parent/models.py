from django.db import models
from rms_api.models import AuditableModel

# Create your models here.
TITLE = (
    ('MR', 'MR'),
    ('MRS', 'MRS'),
)

class Parent(AuditableModel):
    title = models.CharField(max_length=255, choices=TITLE, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    occupation = models.CharField(max_length=255, blank=True)
    parent_phone = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} {self.first_name}"
