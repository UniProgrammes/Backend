from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProgrammeViewSet

router = DefaultRouter()
router.register(r'programmes', ProgrammeViewSet, basename='programme')

urlpatterns = [
    path('api/', include(router.urls)),
]