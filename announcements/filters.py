from django_filters import FilterSet, CharFilter, DateFilter
from .models import Response


class ResponseFilter(FilterSet):
    to_announce = CharFilter(field_name='to_announce__header',
                             label='Введите ключевое слово заголовка объявления',
                             lookup_expr='contains')

    class Meta:
        model = Response
        fields = []
