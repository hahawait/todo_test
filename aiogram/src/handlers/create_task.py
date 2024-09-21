from aiogram import Dispatcher
from aiogram.types import CallbackQuery

from aiogram_dialog import DialogManager
from aiogram_dialog.widgets.kbd import Button

from clients.django import APIClient
from states.tasks import CreateTaskSG


async def create_task(callback: CallbackQuery, _: Button, manager: DialogManager):
    api_client: APIClient = manager.middleware_data['api_client']
    categories = await api_client.get_categories(callback.from_user.id)
    await manager.start(
        CreateTaskSG.waiting_for_title,
        data={'categories': categories, 'user_id': manager.start_data['user_id']}
    )


async def confirm_task(callback: CallbackQuery, _: Button, manager: DialogManager):
    data = manager.dialog_data
    api_client: APIClient = manager.middleware_data['api_client']
    await api_client.create_task(
        user_id=manager.start_data['user_id'],
        title=data['title'],
        description=data['description'],
        due_date=data['due_date'],
        completed=False,
        category_ids=data.get('categories'),
    )
    await callback.message.answer("Задача успешно создана!")
    await manager.done()


def register_handlers(dp: Dispatcher):
    dp.callback_query.register(confirm_task, CreateTaskSG.waiting_for_confirmation)
