from django.contrib import admin
from apps.degrees.models import Degree, DegreeProgramme


class DegreeProgrammeInline(admin.TabularInline):
    model = DegreeProgramme
    extra = 1
    fields = ("programme", "period_years")
    autocomplete_fields = ["programme"]


@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    inlines = [DegreeProgrammeInline]
