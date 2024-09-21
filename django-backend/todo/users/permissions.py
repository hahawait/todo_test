import hashlib
import os
from dotenv import load_dotenv

from rest_framework.permissions import BasePermission

load_dotenv()


class IsFromTelegramBot(BasePermission):
    def has_permission(self, request, view):
        telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        hashed_token = hashlib.sha256(telegram_bot_token.encode()).hexdigest()
        return request.headers.get('Authorization') == f'Bearer {hashed_token}'
