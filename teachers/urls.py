from .views import TeachersViewset
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'teacher', TeachersViewset)

urlpatterns = [
    path('',include(router.urls)),
]
