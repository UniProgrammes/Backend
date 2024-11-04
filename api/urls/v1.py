from django.urls import path, include

urlpatterns = [
    path("", include("apps.programmes.urls")),
    path("", include("apps.users.urls")),
]
