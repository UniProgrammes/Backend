from django.urls import path, include
from rest_framework import routers

from .views import HealthCheckView

router = routers.DefaultRouter()
router.register(
    "",
    HealthCheckView,
    basename="health-check-viewset",
)

urlpatterns = [
    path("", include(router.urls)),
]
