from rest_framework import routers
from django.urls import path, include
from .views import StudentViewSet

router = routers.DefaultRouter()
# StudentViewSet me queryset nahi hai, isliye basename specify karna padega
router.register('students', StudentViewSet, basename='student')

urlpatterns = [
    path('', include(router.urls)),
]
