from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import User, Tenant
from .serializers import UserSerializer, TenantSerializer

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

class TenantViewSet(viewsets.ModelViewSet):
    serializer_class = TenantSerializer
    queryset = Tenant.objects.all()
    permission_classes = [IsAuthenticated]


