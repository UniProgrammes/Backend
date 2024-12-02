from django.contrib import admin
from apps.study_plans.models import StudyPlan, StudyPlanCourse


@admin.register(StudyPlan)
class StudyPlanAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "user")
    search_fields = ("name", "user__username")
    list_filter = ("status",)
    filter_horizontal = ("courses",)
    fieldsets = (
        ("General Information", {
            "fields": ("name", "status", "user")
        }),
        ("Courses", {
            "fields": ("courses",)
        }),
    )


@admin.register(StudyPlanCourse)
class StudyPlanCourseAdmin(admin.ModelAdmin):
    list_display = ("study_plan", "course", "semester", "is_completed")
    search_fields = ("study_plan__name", "course__name")
    list_filter = ("semester", "is_completed")
