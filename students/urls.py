from rest_framework import routers
from .views import ParentViewset, StudentViewset, ParentSerializer
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'student', StudentViewset)
router.register(r'parent', ParentViewset)

urlpatterns = [
    path('', include(router.urls)),
]
