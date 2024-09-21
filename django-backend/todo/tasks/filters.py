import django_filters
from .models import Task


class TaskFilter(django_filters.FilterSet):
    telegram_user_id = django_filters.CharFilter(field_name='user__telegram_user_id', lookup_expr='exact')

    class Meta:
        model = Task
        fields = ['telegram_user_id']
