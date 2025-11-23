from rest_framework import permissions

class IsTenantUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.role == "master_admin":
            return True
        
        return bool(request.user and request.user.is_authenticated and request.user.tenant)

    def has_object_permission(self, request, view, obj):
        if request.user.role == "master_admin":
            return True

        return obj.tenant == request.user.tenant
