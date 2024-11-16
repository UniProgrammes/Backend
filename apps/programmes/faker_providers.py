from faker.providers import BaseProvider


class ProgrammeProvider(BaseProvider):

    def programme_name(self):
        programmes = [
            "Computer Science",
            "Mechanical Engineering",
            "Civil Engineering",
            "Data Science",
            "Artificial Intelligence",
            "Cybersecurity",
            "Software Engineering",
            "Aerospace Engineering",
            "Environmental Engineering",
            "Robotics",
        ]
        return self.random_element(programmes)
