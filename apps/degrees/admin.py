from django.contrib import admin
from apps.degrees.models import Degree, DegreeProgramme


@admin.register(Degree)
class DegreeAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
    filter_horizontal = ("programmes",)


@admin.register(DegreeProgramme)
class DegreeProgrammeAdmin(admin.ModelAdmin):
    list_display = ("degree", "programme", "period_years")
    search_fields = ("degree__name", "programme__name")
    list_filter = ("period_years",)
