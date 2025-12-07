# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import get_user_model

from .permissions import HasApiPermission  # we'll create this next

User = get_user_model()


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        perms = list(request.user.get_all_permissions())
        groups = list(request.user.groups.values_list("name", flat=True))

        return Response({
            "id": request.user.id,
            "username": request.user.username,
            "email": request.user.email,
            "groups": groups,
            "permissions": perms,
        })


class UserManagementView(APIView):
    permission_classes = [IsAuthenticated, HasApiPermission]
    required_permissions = ["api.can_manage_users"]

    def get(self, request):
        users = User.objects.all().values("id", "username", "email")
        return Response({"users": list(users)})
