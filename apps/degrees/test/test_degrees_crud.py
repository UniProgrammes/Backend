from rest_framework.test import APITestCase
from django.urls import reverse
from apps.users.models import User
from apps.degrees.factories import SimpleDegreeFactory

class TestDegreeCrud(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="test", password="test")
        self.client.force_authenticate(user=self.user)
        SimpleDegreeFactory.create_batch(size=2)
        self.degree = SimpleDegreeFactory()

    def test_list_degrees(self):
        url = reverse("degree-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 3)

    def test_retrieve_degree(self):
        url = reverse("degree-detail", args=[str(self.degree.id)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], str(self.degree.id))

    def test_list_without_authentication(self):
        url = reverse("degree-list")
        self.client.force_authenticate(user=None)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

    def test_retrieve_without_authentication(self):
        url = reverse("degree-detail", args=[str(self.degree.id)])
        self.client.force_authenticate(user=None)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)
