from faker import Faker

from apps.courses.faker_providers import CourseProvider


fake = Faker()
fake.add_provider(CourseProvider)
