from django.contrib import admin
from .models import Student, Parent, PrimaryStudent, SecondaryStudent
# Register your models here.

admin.site.register(Parent)
admin.site.register(PrimaryStudent)
admin.site.register(SecondaryStudent)