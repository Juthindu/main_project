# api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .permissions import HasApiPermission
from .models import User


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        perms = [
            p for p in request.user.get_all_permissions()
            if p.startswith("api.")
        ]

        return Response({
            "username": request.user.username,
            "role": request.user.role,
            "permissions": perms,
        })


class UserManagementView(APIView):
    permission_classes = [IsAuthenticated, HasApiPermission]
    required_permissions = ["api.can_manage_users"]

    def get(self, request):
        users = User.objects.all().values("id", "username", "role")
        return Response({"users": list(users)})
