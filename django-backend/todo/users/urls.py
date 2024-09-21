from django.urls import path
from .views import UserCreateView, UserByTelegramIDView

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='user-create'),
    path('by-telegram-id/<str:telegram_user_id>/', UserByTelegramIDView.as_view(), name='user-by-telegram-id'),
]
