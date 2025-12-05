from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    role = models.CharField(max_length=20, default="staff")

    class Meta:
        permissions = [
            ("can_manage_users", "Can manage users"),
            ("can_view_reports", "Can view reports"),
            ("can_edit_courses", "Can edit courses"),
        ]
