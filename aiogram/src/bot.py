import betterlogging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram_dialog import setup_dialogs

from config import get_config

from clients.django import APIClient
from clients.fastapi import APIClient as FastAPIClient

from dialogs.create_comment import create_comment_dialog
from dialogs.create_task import create_task_dialog
from dialogs.get_comments import get_comments_dialog
from dialogs.get_tasks import get_tasks_dialog
from dialogs.menu import main_menu

from handlers.start import register_handlers as register_start_handlers
from handlers.create_task import register_handlers as register_create_task_handlers

betterlogging.basic_colorized_config(level=betterlogging.INFO)

config = get_config()
api_client = APIClient(config)
fastapi_client = FastAPIClient(config)

storage = MemoryStorage()
bot = Bot(token=config.bot.TOKEN)
dp = Dispatcher(storage=storage)

dp.include_router(main_menu)
dp.include_router(create_comment_dialog)
dp.include_router(create_task_dialog)
dp.include_router(get_comments_dialog)
dp.include_router(get_tasks_dialog)

setup_dialogs(dp)

dp['api_client'] = api_client
dp['fast_api_client'] = fastapi_client
register_start_handlers(dp)
register_create_task_handlers(dp)


if __name__ == '__main__':
    dp.run_polling(bot)
