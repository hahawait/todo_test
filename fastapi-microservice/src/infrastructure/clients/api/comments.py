from dataclasses import dataclass

from infrastructure.clients.api.base import APIClient


@dataclass
class CommentsClient(APIClient):
    comments_endpoint: str

    async def create_comment(
        self,
        task_id: str,
        user_id: int,
        content: str,
        token: str,
    ) -> dict:
        """
        Создание комментария к задаче
        """
        response = await self._make_request(
            method="POST",
            url=f"{self.comments_endpoint}",
            json={
                "task": task_id,
                "user": user_id,
                "content": content,
            },
            headers={
                "Authorization": f"Bearer {token}"
            },
        )

        return response.result

    async def get_comments(self, task_id: str, user_id: int, token: str) -> dict:
        """
        Получение комментариев к задаче
        """
        response = await self._make_request(
            method="GET",
            url=f"{self.comments_endpoint}?task={task_id}&user={user_id}",
            headers={
                "Authorization": f"Bearer {token}"
            },
        )
        return response.result

    async def update_comment(self, comment_id: str, content: str, token: str) -> dict:
        """
        Обновление комментария
        """
        response = await self._make_request(
            method="PATCH",
            url=f"{self.comments_endpoint}/{comment_id}/",
            json={"content": content},
            headers={
                "Authorization": f"Bearer {token}"
            },
        )
        return response.result

    async def delete_comment(self, comment_id: str, token: str) -> dict:
        """
        Удаление комментария
        """
        response = await self._make_request(
            method="DELETE",
            url=f"{self.comments_endpoint}/{comment_id}",
            headers={
                "Authorization": f"Bearer {token}"
            },
        )
        return response.result
