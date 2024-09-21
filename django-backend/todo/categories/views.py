from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsFromTelegramBot

from .models import Category
from .serializers import CategorySerializer
from .filters import CategoryFilter


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().distinct()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated | IsFromTelegramBot]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CategoryFilter
