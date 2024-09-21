from aiogram import Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram_dialog import DialogManager

from clients.django import APIClient
from dialogs.menu import MainMenuSG
from states.start import RegistrationSG


async def start(message: Message, state: FSMContext, api_client: APIClient, dialog_manager: DialogManager):
    telegram_user_id = message.from_user.id
    user = await api_client.user_exists(telegram_user_id)
    if not user:
        await message.answer("Вы не зарегистрированы. Пожалуйста, отправьте пароль для регистрации.")
        await state.set_state(RegistrationSG.waiting_for_password)
    else:
        await message.answer("Добро пожаловать обратно!")
        await dialog_manager.start(MainMenuSG.main_menu, data={"user_id": user['user_id']})


async def process_password(message: Message, state: FSMContext, api_client: APIClient, dialog_manager: DialogManager):
    password = message.text
    telegram_user_id = message.from_user.id
    username = message.from_user.username or f"user_{telegram_user_id}"

    user = await api_client.create_user(telegram_user_id, username, password)

    await message.answer("Вы успешно зарегистрированы!")
    await state.set_state(MainMenuSG.main_menu)
    await dialog_manager.start(MainMenuSG.main_menu, data={"user_id": user['user_id']})


def register_handlers(dp: Dispatcher):
    dp.message.register(start, CommandStart())
    dp.message.register(process_password, RegistrationSG.waiting_for_password)
