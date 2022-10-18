from django.urls import path, include
from rest_framework import routers
from .views import ParentViewset

router = routers.DefaultRouter()
router.register(r'', ParentViewset)

urlpatterns = [
    path('', include(router.urls)),
]

