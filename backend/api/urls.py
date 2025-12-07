from django.urls import path
from .views import MeView, UserManagementView

urlpatterns = [
    path("me/", MeView.as_view(), name="me"),
    path("users/", UserManagementView.as_view(), name="users"),
]
