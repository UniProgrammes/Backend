from faker import Faker

from apps.courses.faker_providers import CourseProvider
from apps.programmes.faker_providers import ProgrammeProvider


fake = Faker()
fake.add_provider(CourseProvider)
fake.add_provider(ProgrammeProvider)
