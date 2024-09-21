from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import CustomUser
from .serializers import UserSerializer
from .permissions import IsFromTelegramBot


class UserByTelegramIDView(generics.GenericAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsFromTelegramBot | IsAuthenticated]

    def get(self, request, telegram_user_id):
        try:
            user = CustomUser.objects.get(telegram_user_id=telegram_user_id)
            serializer = self.get_serializer(user)
            data = serializer.data
            data['user_id'] = user.id
            return Response(data, status=status.HTTP_200_OK)
        except CustomUser.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)


class UserCreateView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsFromTelegramBot | AllowAny]

    def perform_create(self, serializer):
        user = serializer.save()
        response_data = serializer.data
        response_data['user_id'] = user.id
        return Response(response_data, status=status.HTTP_201_CREATED)
