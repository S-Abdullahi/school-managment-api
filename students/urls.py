from rest_framework import routers

from .views import ParentViewset, PrimaryStudentViewset, ParentSerializer, SecondaryStudentViewset, SchoolViewset
from django.urls import path, include

router = routers.DefaultRouter('')
router.register(r'', PrimaryStudentViewset)
router.register(r'',SchoolViewset)

router2 = routers.DefaultRouter()
router2.register(r'', SecondaryStudentViewset)

router3 = routers.DefaultRouter()
router3.register(r'', ParentViewset)

router4 = routers.DefaultRouter()
router4.register(r'', SchoolViewset)


urlpatterns = [
    path('school', include(router4.urls)),
    path('parent', include(router3.urls)),
    path('Secondary', include(router2.urls)),
    path('primary', include(router.urls)),
]
