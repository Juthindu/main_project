# api/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    class Meta:
        permissions = [
            ("can_manage_users", "Can manage users"),
            ("can_view_reports", "Can view reports"),
            ("can_edit_courses", "Can edit courses"),
        ]
