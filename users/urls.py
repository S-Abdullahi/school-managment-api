from rest_framework import routers
from .views import UsersViewset
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'user', UsersViewset)

urlpatterns = [
    path('', include(router.urls)),
]
