from rest_framework.test import APITestCase
from django.urls import reverse
from apps.users.models import User
from apps.courses.factories import SimpleCourseFactory

class TestCourseCrud(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(username="test", password="test")
        self.client.force_authenticate(user=self.user)
        SimpleCourseFactory.create_batch(size=3)

    def test_list_courses(self):
        url = reverse("course-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 3)

    def test_retrieve_course(self):
        course = SimpleCourseFactory()
        url = reverse("course-detail", args=[str(course.id)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], str(course.id))

    def test_list_without_authentication(self):
        url = reverse("course-list")
        self.client.force_authenticate(user=None)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

    def test_retrieve_without_authentication(self):
        course = SimpleCourseFactory()
        url = reverse("course-detail", args=[str(course.id)])
        self.client.force_authenticate(user=None)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

    def test_search_course_by_name(self):
        SimpleCourseFactory(name="my custom name")
        url = reverse("course-list")
        response = self.client.get(url, {"name": "my custom name"})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 1)
