from rest_framework.permissions import BasePermission

class HasApiPermission(BasePermission):
    """
    Check if the user has all required API permissions.
    View must define `required_permissions = [...]`.
    """

    message = "You do not have permission to perform this action."

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        required = getattr(view, "required_permissions", [])
        if not required:
            return True  # no extra permissions required

        user_perms = request.user.get_all_permissions()

        # must have ALL required permissions
        for perm in required:
            if perm not in user_perms:
                return False

        return True
