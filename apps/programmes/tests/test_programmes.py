from rest_framework.test import APITestCase
from django.urls import reverse
from apps.users.models import User
from apps.programmes.factories import SimpleProgrammeFactory
from apps.courses.factories import SimpleCourseFactory


class TestProgrammeCrud(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="test", password="test")
        self.client.force_authenticate(user=self.user)
        SimpleProgrammeFactory.create_batch(size=2)
        self.programme = SimpleProgrammeFactory()
        courses = SimpleCourseFactory.create_batch(size=3)
        for course in courses:
            self.programme.programmecourse_set.create(
                course=course,
                year=1,
            )

    def test_list_programmes(self):
        url = reverse("programme-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 3)

    def test_retrieve_programme(self):
        url = reverse("programme-detail", args=[str(self.programme.id)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], str(self.programme.id))

    def test_list_without_authentication(self):
        url = reverse("programme-list")
        self.client.force_authenticate(user=None)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 3)

    def test_retrieve_without_authentication(self):
        url = reverse("programme-detail", args=[str(self.programme.id)])
        self.client.force_authenticate(user=None)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], str(self.programme.id))

    def test_courses(self):
        url = reverse("programme-courses", args=[str(self.programme.id)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["programme"]["id"], str(self.programme.id))
        self.assertEqual(len(response.data["courses"]), 3)
