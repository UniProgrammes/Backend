from rest_framework.test import APITestCase
from django.urls import reverse

from apps.users.factories import UserFactory

class CreateUserTest(APITestCase):
    def setUp(self) -> None:
        self.user = UserFactory(username="test")
        self.user.set_password("test")
        self.user.save()

    def test_create_user(self):
        url = reverse("users-register")
        data = {
            "username": "test1",
            "first_name": "Test",
            "middle_name": "test",
            "last_name": "Test",
            "email": "test1@gmail.com",
            "enrollment_number": "10676352",
            "password": "Hello1234"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)
        self.assertIn("username", response.data)
        self.assertEqual(response.data["username"], "test1")

    def test_login(self):
        url = reverse("token_obtain_pair")
        data = {
            "username": "test",
            "password": "test"
        }
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_get_me(self):
        url = reverse("users-me")
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["username"], "test")
        self.assertEqual(response.data["first_name"], self.user.first_name)
        self.assertEqual(response.data["last_name"], self.user.last_name)
        self.assertEqual(response.data["email"], self.user.email)
        self.assertEqual(response.data["enrollment_number"], self.user.enrollment_number)

    def test_update_me(self):
        url = reverse("users-me")
        self.client.force_authenticate(user=self.user)
        response = self.client.patch(url, {"first_name": "New Name"}, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["first_name"], "New Name")
