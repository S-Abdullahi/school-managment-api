from django.db import models  
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin  
from django.utils import timezone  
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager 
import uuid 
# Create your models here.  
  
  
  
class User(AbstractBaseUser, PermissionsMixin):  
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(_('email_address'), unique=True, max_length = 200)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    phone = models.CharField(max_length=255, blank=True)  
    date_joined = models.DateTimeField(default=timezone.now)  
    is_staff = models.BooleanField(default=False)  
    is_active = models.BooleanField(default=True)  
      
  
  
    USERNAME_FIELD = 'email'  
    REQUIRED_FIELDS = []  
  
    objects = CustomUserManager()  
      
    def has_perm(self, perm, obj=None):  
        "Does the user have a specific permission?"  
        # Simplest possible answer: Yes, always  
        return True  
  
    @property  
    def is_admin(self):  
        "Is the user a admin member?"  
        return self.admin  
  
    def __str__(self):  
        return self.email  