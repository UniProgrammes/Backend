from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from apps.users.models import User
from apps.questions.models import Question

class CreateQuestionAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@gmail.com",
            password="testpassword123"
        )
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.url = reverse('create-question')

    def test_create_question(self):
        data = {
            "text": "What is Uniprogrammers?",
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.data)
        self.assertEqual(response.data["text"], "What is Uniprogrammers?")
        self.assertEqual(response.data["user"], (self.user.id))


class GetUserQuestionsAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username="testuser",
            email="testuser@gmail.com",
            password="testpassword123"
        )
        self.token = RefreshToken.for_user(self.user).access_token
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {self.token}")
        self.url = reverse('user-questions')

        # Crea alcune domande
        Question.objects.create(
            user=self.user,
            text="What is Uniprogrammers?"
        )
        Question.objects.create(
            user=self.user,
            text="How does Uniprogrammers handle study plans?"
        )

    def test_get_user_questions(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(
            response.data[0]["text"],
            "What is Uniprogrammers?"
            )
        self.assertEqual(
            response.data[1]["text"],
            "How does Uniprogrammers handle study plans?"
            )
