from django.test import TestCase
from django.urls import reverse

class ExampleTestCase(TestCase):
    def test_example(self):
        self.assertEqual(1 + 1, 2)


class CreateUserTestAssertEqual(TestCase):
    def test_create_user(self):
        url = reverse('users-register')  # Il nome dell'URL nel file urls.py
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
        self.assertEqual(response.status_code, 201)  # 201: Created
        self.assertIn("username", response.data)
        self.assertEqual(response.data["username"], "test1")

class CreateUserTestAssertNotEqual(TestCase):
    def test_create_user(self):
        url = reverse('users-register')  # Il nome dell'URL nel file urls.py
        data = {
            "username": "test2",
            "first_name": "Test",
            "middle_name": "test",
            "last_name": "Test",
            "email": "test2@gmail.com",
            "enrollment_number": "10676352",
            "password": "Hello1234"
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 201)  # 201: Created
        self.assertIn("username", response.data)
        self.assertNotEqual(response.data["username"], "Error")
