from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User
from expenses_entries.models import ExpenseEntrie

class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.user.is_authenticated:
            return True
        return False

class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        return obj == request.user

class IsExpenseEntrieOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: ExpenseEntrie) -> bool:
        return obj.user_id == request.user.id
