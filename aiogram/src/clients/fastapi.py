import aiohttp
from config import Config


class APIClient:
    def __init__(self, config: Config):
        self.base_url = config.fastapi.FASTAPI_BASE_URL
        self.config = config

    async def create_comment(
        self,
        user_id: int,
        task_id: str,
        content: str
    ):
        async with aiohttp.ClientSession() as session:
            async with session.post(
                f"{self.base_url}/comments/",
                json={
                    "user": user_id,
                    "task": task_id,
                    "content": content
                },
                headers={"Authorization": f"Bearer {self.config.bot.HASHED_TOKEN}"}
            ) as response:
                return await response.json()

    async def get_comments(self, task_id: str, user_id: int):
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.base_url}/comments/{task_id}?user_id={user_id}",
                headers={
                    "Authorization": f"Bearer {self.config.bot.HASHED_TOKEN}"
                }
            ) as response:
                return await response.json()
