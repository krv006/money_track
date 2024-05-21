# permissions.py
from rest_framework.permissions import BasePermission

class IsAuth(BasePermission):
    """
    Custom permission to only allow authenticated users to access the view.
    """
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated
