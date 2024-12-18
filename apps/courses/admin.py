from django.contrib import admin
from apps.courses.models import Course


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = (
        "name", 
        "code", 
        "credits", 
        "educational_level", 
        "main_area", 
        "semester", 
        "get_period_display",
    )
    search_fields = ("name", "code", "main_area")
    list_filter = ("main_area", "educational_level", "semester", "period")
    filter_horizontal = ("learning_outcomes", "prerequisites")

    fieldsets = (
        ("Course Information", {
            "fields": ("name", "code", "credits", "educational_level", "description", "main_area")
        }),
        ("Schedule", {
            "fields": ("semester", "period")
        }),
        ("Relationships", {
            "fields": ("learning_outcomes", "prerequisites")
        }),
    )

    def get_period_display(self, obj):
        return obj.get_period_display()

    get_period_display.short_description = "Period"
