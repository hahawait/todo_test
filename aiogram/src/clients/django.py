import aiohttp
from config import Config


class APIClient:
    def __init__(self, config: Config):
        self.base_url = config.django.DJANGO_BASE_URL
        self.config = config

    async def user_exists(self, telegram_user_id: int) -> bool:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{self.base_url}/api/users/by-telegram-id/{telegram_user_id}/", headers={
                "Authorization": f"Bearer {self.config.bot.HASHED_TOKEN}"
            }) as response:
                if response.status == 200:
                    return await response.json()
                return False

    async def create_user(self, telegram_user_id: int, username: str, password: str):
        async with aiohttp.ClientSession() as session:
            async with session.post(f"{self.base_url}/api/users/create/", json={
                "telegram_user_id": telegram_user_id,
                "username": username,
                "password": password
            }) as response:
                return await response.json()

    async def get_tasks(self, telegram_user_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.base_url}/api/tasks/",
                params={"telegram_user_id": telegram_user_id},
                headers={
                    "Authorization": f"Bearer {self.config.bot.HASHED_TOKEN}"
                }
            ) as response:
                return await response.json()

    async def create_task(
        self,
        user_id: int,
        title: str,
        description: str,
        due_date: str,
        completed: bool,
        category_ids: list[str]
    ):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/api/tasks/",
                json={
                    "user": user_id,
                    "title": title,
                    "description": description,
                    "due_date": due_date,
                    "completed": completed,
                    "category": category_ids
                },
                headers={"Authorization": f"Bearer {self.config.bot.HASHED_TOKEN}"}
            ) as response:
                return await response.json()

    async def get_categories(self, telegram_user_id: int) -> list[int]:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.base_url}/api/categories/",
                params={"telegram_user_id": telegram_user_id},
                headers={"Authorization": f"Bearer {self.config.bot.HASHED_TOKEN}"}
            ) as response:
                return await response.json()

    async def create_categories(self, name: str):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/api/categories/",
                json={"name": name},
                headers={"Authorization": f"Bearer {self.config.bot.HASHED_TOKEN}"}
            ) as response:
                return await response.json()
