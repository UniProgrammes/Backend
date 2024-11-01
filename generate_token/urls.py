from django.urls import path
from .views import GenerateTokenView

urlpatterns = [
    path('api/generate_token/', GenerateTokenView.as_view(), name='generate-token'),
]