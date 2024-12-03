from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("apps.health.urls")),
    path("admin/", admin.site.urls),
    path("v1/", include("api.urls.v1")),
]
