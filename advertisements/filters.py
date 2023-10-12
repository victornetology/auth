from django_filters import rest_framework as filters, DateFromToRangeFilter, DateTimeFilter, ChoiceFilter

from advertisements.models import Advertisement, AdvertisementStatusChoices


class AdvertisementFilter(filters.FilterSet):
    """Фильтры для объявлений."""

    """ Фильтрация по дате  _after & _before"""
    created_at = DateFromToRangeFilter()
    updated_at = DateFromToRangeFilter()

    # фильтрация по дате
    status = ChoiceFilter(choices=AdvertisementStatusChoices.choices)

    class Meta:
        model = Advertisement
        # поля, по которым можно осуществлять фильтрацию
        fields = ['created_at', 'updated_at', 'creator', 'status']
