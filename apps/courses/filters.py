from django_filters import FilterSet, CharFilter


class CourseFilter(FilterSet):
    name = CharFilter(lookup_expr="icontains")
