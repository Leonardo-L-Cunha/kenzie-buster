from rest_framework import permissions
from rest_framework.views import Request, View

class isOwnerUser(permissions.BasePermission):
    def has_object_permission(self, request:Request, view:View, obj):
        if request.user.is_employee:
                return True
        if obj == request.user:
                return True
        return False
            