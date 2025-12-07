# api/permissions.py
from rest_framework.permissions import BasePermission


class HasApiPermission(BasePermission):
    message = "You do not have permission to perform this action."

    def has_permission(self, request, view):
        user = request.user
        if not user or not user.is_authenticated:
            return False

        required = getattr(view, "required_permissions", [])
        if not required:
            return True

        user_perms = user.get_all_permissions()
        for perm in required:
            if perm not in user_perms:
                return False

        return True
