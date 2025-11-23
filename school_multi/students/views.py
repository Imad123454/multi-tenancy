from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Student
from .serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user

        # MASTER ADMIN CAN SEE EVERYTHING
        if user.role == 'master_admin':
            return Student.objects.all()

        # DIRECTOR CAN SEE ONLY ITS OWN TENANT
        return Student.objects.filter(tenant=user.tenant_id)

    def perform_create(self, serializer):
        serializer.save(tenant=self.request.user.tenant)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)