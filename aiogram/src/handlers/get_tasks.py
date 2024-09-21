from aiogram.types import CallbackQuery
from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from clients.django import APIClient
from states.tasks import GetTasksSG
from states.menu import MainMenuSG


async def get_tasks(callback: CallbackQuery, _: Button, manager: DialogManager):
    api_client: APIClient = manager.middleware_data['api_client']
    tasks = await api_client.get_tasks(callback.message.chat.id)
    await manager.start(
        GetTasksSG.showing_task,
        data={'tasks': tasks, 'current_index': 0, 'user_id': manager.start_data['user_id']}
    )


async def show_task(dialog_manager: DialogManager, **kwargs):
    data = dialog_manager.start_data
    tasks = data['tasks']
    current_index = data['current_index']
    if tasks:
        task = tasks[current_index]
        task_info = (
            f"Задача: {task['title']}\n"
            f"Описание: {task['description']}\n"
            f"Дата выполнения: {task['due_date']}\n"
            f"Выполнено: {'Да' if task['completed'] else 'Нет'}\n"
            f"Категории: {', '.join([cat['name'] for cat in task['category_details']])}"
        )
    else:
        task_info = ("Вы не добавили ни одной задачи.\nВернитесь в меню и добавьте задачу.")
    return {'task': task_info}


async def next_task(callback: CallbackQuery, _: Button, manager: DialogManager):
    data = manager.start_data
    if data['current_index'] < len(data['tasks']) - 1:
        data['current_index'] += 1
    await manager.switch_to(GetTasksSG.showing_task)


async def prev_task(callback: CallbackQuery, _: Button, manager: DialogManager):
    data = manager.start_data
    if data['current_index'] > 0:
        data['current_index'] -= 1
    await manager.switch_to(GetTasksSG.showing_task)


async def back_to_menu(callback: CallbackQuery, _: Button, manager: DialogManager):
    await manager.start(MainMenuSG.main_menu, data={"user_id": manager.start_data['user_id']})
