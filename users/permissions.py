from rest_framework import permissions
from rest_framework.views import Request, View
from .models import User
from expenses_entries.models import ExpenseEntrie
from credit_cards.models import Credit_Card

class IsAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.user.is_authenticated:
            return True
        return False

class IsAccountOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: User) -> bool:
        if obj == request.user or request.user.is_superuser == True:
            return True
        return False

class IsExpenseEntrieOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: ExpenseEntrie) -> bool:
        if obj.user_id == request.user.id or request.user.is_superuser == True:
            return True
        return False

class IsCreditCardOwner(permissions.BasePermission):
    def has_object_permission(self, request, view: View, obj: Credit_Card) -> bool:
        if obj.user_id == request.user.id or request.user.is_superuser == True:
            return True
        return False

class RoutePermission(permissions.BasePermission):
    def has_permission(self, request, view) -> bool:
        if request.method == 'GET' and request.user.is_superuser == True:
            return True
        if request.method == 'GET' and request.user.is_superuser == False:
            return False
        if request.method == 'POST' and request.user.is_superuser == True or request.user.is_superuser == False:
            return True
        return False
