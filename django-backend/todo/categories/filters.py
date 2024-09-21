import django_filters
from .models import Category


class CategoryFilter(django_filters.FilterSet):
    telegram_user_id = django_filters.CharFilter(field_name='tasks__user__telegram_user_id', lookup_expr='exact')

    class Meta:
        model = Category
        fields = ['telegram_user_id']
