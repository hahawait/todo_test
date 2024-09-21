import hashlib
import os
from dotenv import load_dotenv

from rest_framework.authentication import BaseAuthentication

load_dotenv()


class TelegramBotAuthentication(BaseAuthentication):
    def authenticate(self, request):
        telegram_bot_token = os.getenv('TELEGRAM_BOT_TOKEN')
        hashed_token = hashlib.sha256(telegram_bot_token.encode()).hexdigest()
        auth_header = request.headers.get('Authorization')

        if auth_header == f'Bearer {hashed_token}':
            return (None, None)
        return None
