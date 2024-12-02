from django.contrib import admin
from apps.programmes.models import Programme, ProgrammeCourse


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ("name", "degree_type", "credits")
    search_fields = ("name", "degree_type")
    list_filter = ("degree_type",)
    filter_horizontal = ("courses",)


@admin.register(ProgrammeCourse)
class ProgrammeCourseAdmin(admin.ModelAdmin):
    list_display = ("programme", "course", "year", "period_months", "is_mandatory")
    search_fields = ("programme__name", "course__name")
    list_filter = ("is_mandatory", "year", "period_months")
