from rest_framework import permissions
from rest_framework.views import Request, View

class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.user.is_authenticated:
            return True
        return False