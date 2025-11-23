from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'tenant']
    list_filter = ['tenant'] 

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.role == 'master_admin':
            return qs  
        return qs.filter(tenant=request.user.tenant)  
         