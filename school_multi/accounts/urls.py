from rest_framework import routers
from django.urls import path, include
from .views import UserViewSet, TenantViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('tenants', TenantViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
