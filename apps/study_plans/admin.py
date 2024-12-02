from django.contrib import admin
from apps.study_plans.models import StudyPlan, StudyPlanCourse


class StudyPlanCourseInline(admin.TabularInline):
    model = StudyPlanCourse
    extra = 1
    fields = ("course", "semester", "is_completed")
    autocomplete_fields = ["course"]


@admin.register(StudyPlan)
class StudyPlanAdmin(admin.ModelAdmin):
    list_display = ("name", "status", "user")
    search_fields = ("name", "user__username")
    list_filter = ("status",)
    inlines = [StudyPlanCourseInline]
