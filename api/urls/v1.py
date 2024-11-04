from django.urls import path, include

urlpatterns = [
    path("", include("apps.programme.urls")),
    path("", include("apps.course.urls")),
]
