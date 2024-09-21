from typing import Annotated

from fastapi import Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import jwt, ExpiredSignatureError, JWTError

from app.api.schemas import UserSchema
from config import Config, get_config


class AuthCredentials:
    """
    Зависимость, подтверждающая аутентификацию юзера через JWT.
    Возвращает даные о юзере, полученные в payload токена
    """

    def __init__(self, config: Config) -> None:
        self.config = config

    def __call__(
            self,
            credentials: Annotated[HTTPAuthorizationCredentials, Depends(HTTPBearer())]
    ) -> UserSchema:
        """
        :param credentials: Зависимость из FastAPI security. Проверяет наличие заголовка "Authorization" и схемы Bearer.
        Возвращает схему и сам токен
        :return: Данные о пользователе, полученные из payload токена
        """
        try:
            if self.is_telegram_token(credentials.credentials):
                user_data = self.decode_telegram_token(credentials.credentials)
            else:
                payload = jwt.decode(
                    credentials.credentials,
                    self.config.auth_config.PUBLIC_KEY,
                    self.config.auth_config.ALGORITHM
                )
                user_data = UserSchema(token=credentials.credentials, **payload)

            if not user_data:
                raise HTTPException(status_code=401, detail="Token is not correct")

            return user_data

        except (ExpiredSignatureError, JWTError) as e:
            if isinstance(e, ExpiredSignatureError):
                raise HTTPException(status_code=401, detail="Token is expired")
            else:
                raise HTTPException(status_code=401, detail="Token is not correct")

    def is_telegram_token(self, token: str) -> bool:
        return token == self.config.bot.HASHED_TOKEN

    def decode_telegram_token(self, token: str) -> UserSchema:
        return UserSchema(token=token, id=0, email=None, name=None)


def get_user():
    return AuthCredentials(config=get_config())
