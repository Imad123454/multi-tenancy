from django.contrib import admin
from .models import User, Tenant

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username','email','role','tenant']

@admin.register(Tenant)
class TenantAdmin(admin.ModelAdmin):
    list_display = ['name']
