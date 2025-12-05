from django.contrib import admin
from django.urls import path, include
from api.jwt import MyTokenView
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),

    path("api/token/", MyTokenView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),

    path("api/", include("api.urls")),  # all the rest of your API
]
