from django.urls import path, include

urlpatterns = [
    path("", include("apps.courses.urls")),
    path("", include("apps.programmes.urls")),
    path("", include("apps.study_plans.urls")),
    path("", include("apps.users.urls")),
    path("", include("apps.degrees.urls")),
    path("", include("apps.learning_outcomes.urls")),
    path("", include("apps.questions.urls")),
]
