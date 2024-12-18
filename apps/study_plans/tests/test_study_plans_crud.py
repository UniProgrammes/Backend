from rest_framework.test import APITestCase
from django.urls import reverse
from apps.users.factories import UserFactory
from apps.study_plans.factories import StudyPlanFactory, StudyPlanCourseFactory
from apps.courses.factories import SimpleCourseFactory
from apps.study_plans.models import StudyPlan

class TestStudyPlanCrud(APITestCase):
    def setUp(self) -> None:
        # Set up authenticated user
        self.user = UserFactory()
        self.client.force_authenticate(user=self.user)
        StudyPlanFactory.create_batch(size=2, user=self.user)
        self.study_plan = StudyPlanFactory(user=self.user)
        StudyPlanCourseFactory(study_plan=self.study_plan)
        StudyPlanCourseFactory(study_plan=self.study_plan)

    def test_list_study_plans(self):
        url = reverse("study-plan-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data["results"]), 3)

    def test_retrieve_study_plan(self):
        url = reverse("study-plan-detail", args=[str(self.study_plan.id)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["id"], str(self.study_plan.id))

    def test_list_without_authentication(self):
        url = reverse("study-plan-list")
        self.client.force_authenticate(user=None)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

    def test_retrieve_without_authentication(self):
        url = reverse("study-plan-detail", args=[str(self.study_plan.id)])
        self.client.force_authenticate(user=None)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 401)

    def test_create_study_plan(self):
        url = reverse("study-plan-list")
        response = self.client.post(url, {"name": "Test Study Plan"})
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.data["name"], "Test Study Plan")
        self.assertEqual(response.data["user"], self.user.id)

    def test_update_study_plan(self):
        url = reverse("study-plan-detail", args=[str(self.study_plan.id)])
        response = self.client.patch(url, {"name": "Updated Study Plan"})
        self.assertEqual(response.status_code, 200)
        self.study_plan.refresh_from_db()
        self.assertEqual(self.study_plan.name, "Updated Study Plan")

    def test_delete_study_plan(self):
        url = reverse("study-plan-detail", args=[str(self.study_plan.id)])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, 204)
        self.assertFalse(StudyPlan.objects.filter(id=self.study_plan.id).exists())

    def test_study_plan_courses(self):
        url = reverse("study-plan-courses", args=[str(self.study_plan.id)])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 2)

    def test_delete_course_from_study_plan(self):
        url = reverse("study-plan-courses", args=[str(self.study_plan.id)])
        print(self.study_plan.courses.first().id)
        response = self.client.delete(url, {
            "courses_ids": [str(course.id) for course in self.study_plan.courses.all()]
        }, format="json")
        self.assertEqual(response.status_code, 204)
        self.assertFalse(self.study_plan.courses.exists())

    def test_add_course_to_study_plan(self):
        url = reverse("study-plan-courses", args=[str(self.study_plan.id)])
        new_course = SimpleCourseFactory()
        response = self.client.post(url, {
            "courses": [
                {
                    "id": str(new_course.id)
                }
            ]
        }, format="json")
        self.assertEqual(response.status_code, 204)
        self.assertEqual(self.study_plan.courses.count(), 3)
