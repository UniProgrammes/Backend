from faker.providers import BaseProvider


class CourseProvider(BaseProvider):

    def course_name(self):
        topics = [
            "Programming", "Data Structures", "Operating Systems",
            "Artificial Intelligence", "Machine Learning", "Computer Networks",
            "Cybersecurity", "Database Management", "Web Development",
            "Cloud Computing", "Human-Computer Interaction", "Software Engineering",
            "Distributed Systems", "Big Data Analytics", "Blockchain",
            "Natural Language Processing", "Quantum Computing", "Data Mining",
            "Game Development", "Mobile App Development",
            "Thermodynamics", "Fluid Mechanics", "Heat Transfer",
            "Dynamics", "Robotics", "Materials Science",
            "Control Systems", "Mechanical Design", "Manufacturing Processes",
            "Energy Systems", "Computational Mechanics", "Finite Element Analysis",
            "Automotive Engineering", "Aerospace Engineering",
            "Advanced Dynamics", "Kinematics", "Industrial Automation",
            "Microfluidics", "Sustainable Engineering", "Precision Engineering",
            "Structural Engineering", "Geotechnical Engineering",
            "Construction Management", "Environmental Engineering",
            "Hydraulics", "Surveying", "Pavement Design",
            "Earthquake Engineering", "Bridge Design", "Coastal Engineering",
            "Urban Planning", "Soil Mechanics", "Smart Cities",
            "Infrastructure Design", "Energy-Efficient Buildings",
            "Flood Risk Management", "Building Information Modeling (BIM)",
            "Risk Assessment", "Sustainable Construction",
            "Data Science", "Data Visualization", "Neural Networks",
            "Big Data Analytics", "Predictive Modeling",
            "Statistical Inference", "Reinforcement Learning",
            "Ethics in AI", "Deep Learning", "Bayesian Statistics",
            "Time Series Analysis", "Applied Machine Learning",
            "Experimental Design", "Graph Analytics", "AI for Decision Making",
            "Feature Engineering", "Practical Data Science",
            "Cloud Data Engineering", "Real-Time Analytics", "Advanced Analytics",
            "Digital Transformation", "Ethical Hacking",
            "Renewable Energy Systems", "Augmented Reality",
            "Virtual Reality", "Bioinformatics", "Biomechanics",
            "Environmental Impact Assessment", "Smart Infrastructure",
            "Additive Manufacturing", "Sustainability in Design",
        ]
        return f"{self.random_element(topics)}"
