from django_filters import rest_framework as filters, DateFromToRangeFilter, DateTimeFilter

from advertisements.models import Advertisement


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    # TODO: задайте требуемые фильтры
    created_at = DateTimeFilter(field_name='created_at',
                                       lookup_expr='gte')

    created_at_before = DateFromToRangeFilter(field_name='created_at')

    class Meta:
        model = Advertisement
        fields = ['createdAt']

