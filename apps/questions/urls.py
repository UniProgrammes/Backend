from django.urls import path
from .views import CreateQuestionAPI, UserQuestionsAPI

urlpatterns = [
    path('questions/', CreateQuestionAPI.as_view(), name='create-question'),
    path('questions/user/', UserQuestionsAPI.as_view(), name='user-questions'),
]
