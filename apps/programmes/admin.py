from django.contrib import admin
from apps.programmes.models import Programme, ProgrammeCourse


class ProgrammeCourseInline(admin.TabularInline):
    model = ProgrammeCourse
    extra = 1
    fields = ("course", "year", "period_months", "is_mandatory")
    autocomplete_fields = ["course"]


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ("name", "degree_type", "credits")
    search_fields = ("name", "degree_type")
    list_filter = ("degree_type",)
    inlines = [ProgrammeCourseInline]
