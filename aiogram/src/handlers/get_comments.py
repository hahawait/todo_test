from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from clients.fastapi import APIClient
from states.comments import GetCommentsSG
from states.menu import MainMenuSG


async def get_comments(callback: CallbackQuery, _: Button, manager: DialogManager):
    api_client: APIClient = manager.middleware_data['fast_api_client']
    data = manager.start_data
    task_idx = data["current_index"]
    task = data["tasks"][task_idx]
    comments = await api_client.get_comments(task["id"], data["user_id"])
    await manager.start(
        GetCommentsSG.showing_comments,
        data={
            'comments': comments,
            'current_index': 0,
            'user_id': data['user_id']
        }
    )


async def show_comment(dialog_manager: DialogManager, **kwargs):
    data = dialog_manager.start_data
    comments = data['comments']
    current_index = data['current_index']
    if comments:
        comment = comments[current_index]
        comments_info = (
            f"Комментарий: {comment['content']}\n"
        )
    else:
        comments_info = (
            f"Вы не добавили комментарии к этой задаче\n"
        )
    return {'comment': comments_info}


async def next_comment(callback: CallbackQuery, _: Button, manager: DialogManager):
    data = manager.start_data
    if data['current_index'] < len(data['comments']) - 1:
        data['current_index'] += 1
    await manager.switch_to(GetCommentsSG.showing_comments)


async def prev_comment(callback: CallbackQuery, _: Button, manager: DialogManager):
    data = manager.start_data
    if data['current_index'] > 0:
        data['current_index'] -= 1
    await manager.switch_to(GetCommentsSG.showing_comments)


async def back_to_menu(callback: CallbackQuery, _: Button, manager: DialogManager):
    await manager.start(MainMenuSG.main_menu, data={"user_id": manager.start_data['user_id']})
