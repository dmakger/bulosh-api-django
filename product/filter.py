import django_filters
from django.db.models import Q

from .models import Product


class ProductFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(method='search_by_all_fields', label='Поиск по всем полям')
    category_id = django_filters.NumberFilter(field_name='category_id', label='ID категории')

    class Meta:
        model = Product
        fields = {
            'name': ['icontains'],
        }

    def search_by_all_fields(self, queryset, name, value):
        return queryset.filter(
            Q(name__icontains=value) |
            Q(category__name__icontains=value)
        )
