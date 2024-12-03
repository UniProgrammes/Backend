from django.contrib import admin
from apps.courses.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "credits", "educational_level", "main_area")
    search_fields = ("name", "code", "main_area")
    list_filter = ("main_area", "educational_level")
    filter_horizontal = ("learning_outcomes", "prerequisites")
    fieldsets = (
        ("Course Information", {
            "fields": ("name", "code", "credits", "educational_level", "description", "main_area")
        }),
        ("Relationships", {
            "fields": ("learning_outcomes", "prerequisites")
        }),
    )
