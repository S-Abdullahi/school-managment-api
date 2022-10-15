from django.urls import path, include
from rest_framework import routers
from .views import TeacherViewset

router = routers.DefaultRouter()
router.register(r'teacher',TeacherViewset)

urlpatterns = [
    path('',include(router.urls)),
]
