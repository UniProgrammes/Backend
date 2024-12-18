from django.contrib import admin
from apps.programmes.models import Programme, ProgrammeCourse


class ProgrammeCourseInline(admin.TabularInline):
    model = ProgrammeCourse
    extra = 1
    fields = ("course", "year", "is_mandatory")
    autocomplete_fields = ["course"]


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ("name", "degree_type", "credits")
    search_fields = ("name", )
    inlines = [ProgrammeCourseInline]

    def degree_type(self, obj):
        return obj.degree_type
    degree_type.short_description = "Degree Type"
