from django_filters import FilterSet, CharFilter


class ProgrammeFilter(FilterSet):
    name = CharFilter(lookup_expr="icontains")
