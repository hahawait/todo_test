from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from clients.fastapi import APIClient
from states.comments import CreateCommentSG
from states.menu import MainMenuSG


async def create_comment(callback: CallbackQuery, _: Button, manager: DialogManager):
    data = manager.start_data
    task_idx = data["current_index"]
    task = data["tasks"][task_idx]
    await manager.start(
        CreateCommentSG.waiting_for_comment,
        data={
            'task_id': task["id"],
            **data
        }
    )


async def confirm_comment(callback: CallbackQuery, _: Button, manager: DialogManager):
    api_client: APIClient = manager.middleware_data['fast_api_client']
    await api_client.create_comment(
        manager.start_data["user_id"],
        manager.start_data["task_id"],
        manager.dialog_data["comment"]
    )
    await callback.message.answer("Комментарий успешно добавлен!")
    await manager.done()
    await manager.start(
        MainMenuSG.main_menu,
        data={"user_id": manager.start_data["user_id"]}
    )
