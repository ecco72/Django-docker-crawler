import django_filters
from .models import AgodaData

class AgodaDataFilter(django_filters.FilterSet):
    # SQL 中的 LIKE
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    loc = django_filters.CharFilter(field_name='loc', lookup_expr='icontains')
    # 價格過濾
    price_min = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price_max = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = AgodaData
        fields = ['title', 'loc', 'price_min', 'price_max']
