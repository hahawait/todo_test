from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from django_filters.rest_framework import DjangoFilterBackend

from users.permissions import IsFromTelegramBot

from .filters import TaskFilter
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.select_related('user').prefetch_related('category').all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated | IsFromTelegramBot]
    filter_backends = [DjangoFilterBackend]
    filterset_class = TaskFilter

    def get_queryset(self):
        return Task.objects.select_related('user').prefetch_related('category')
