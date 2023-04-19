from django_filters import rest_framework as filters
from reviews.models import Title


class TitleFilter(filters.FilterSet):

    genre = filters.Filter(
        field_name='genre__slug',
        lookup_expr='icontains'
    )
    category = filters.Filter(
        field_name='category__slug',
        lookup_expr='icontains'
    )
    name = filters.Filter(
        field_name='name',
        lookup_expr='icontains'
    )
    year = filters.Filter(
        field_name='year',
        lookup_expr='icontains'
    )

    class Meta:
        model = Title
        fields = ('name', 'year', 'category', 'genre')
