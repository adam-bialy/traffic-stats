from rest_framework.permissions import BasePermission
from rest_framework.permissions import IsAuthenticated


class APIPermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return bool(request.user and request.user.is_authenticated)
        return True
