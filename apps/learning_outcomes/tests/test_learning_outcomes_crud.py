from rest_framework.test import APITestCase
from django.urls import reverse
from apps.users.models import User
from apps.learning_outcomes.factories import LearningOutcomeFactory


class TestLearningOutcomeCrud(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="test", password="test")
        self.client.force_authenticate(user=self.user)
        LearningOutcomeFactory.create_batch(size=2)
        self.learning_outcome = LearningOutcomeFactory()

    def test_list_learning_outcomes(self):
        url = reverse("learning-outcome-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 3)

    def test_retrieve_learning_outcome(self):
        url = reverse("learning-outcome-detail", args=[str(self.learning_outcome.id)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], str(self.learning_outcome.id))

    def test_list_without_authentication(self):
        url = reverse("learning-outcome-list")
        self.client.force_authenticate(user=None)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 3)

    def test_retrieve_without_authentication(self):
        url = reverse("learning-outcome-detail", args=[str(self.learning_outcome.id)])
        self.client.force_authenticate(user=None)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], str(self.learning_outcome.id))
