from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.degrees.views import DegreeViewSet

router = DefaultRouter()
router.register("degrees", DegreeViewSet, basename="degree")

urlpatterns = [
    path("", include(router.urls)),
]
