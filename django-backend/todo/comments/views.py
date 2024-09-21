from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from users.permissions import IsFromTelegramBot

from .filters import CommentFilter
from .models import Comment
from .serializers import CommentSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.select_related('user', 'task').all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated | IsFromTelegramBot]
    filter_backends = [DjangoFilterBackend]
    filterset_class = CommentFilter
