from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Question
from .serializers import QuestionSerializer

class CreateQuestionAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        data = request.data.copy()
        data['user'] = user.id
        data['user_email'] = user.email

        serializer = QuestionSerializer(data=data, context={'user': user})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class UserQuestionsAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        questions = Question.objects.filter(user=user)
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data, status=200)