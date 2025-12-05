# api/urls.py
from django.urls import path
from .views import MeView, UserManagementView  # remove ReportsView for now

urlpatterns = [
    path("me/", MeView.as_view(), name="me"),
    path("users/", UserManagementView.as_view(), name="users"),
]