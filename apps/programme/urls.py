from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.programme.views import ProgrammeViewSet

router = DefaultRouter()
router.register("programmes", ProgrammeViewSet, basename="programme")

urlpatterns = [
    path("", include(router.urls)),
]