from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Row, Button
from aiogram_dialog.widgets.text import Const

from states.menu import MainMenuSG
from handlers.create_task import create_task
from handlers.get_tasks import get_tasks

main_menu = Dialog(
    Window(
        Const("Выберите действие:"),
        Row(
            Button(Const("Просмотреть задачи"), id="view_tasks", on_click=get_tasks),
            Button(Const("Добавить задачу"), id="add_task", on_click=create_task),
        ),
        state=MainMenuSG.main_menu
    ),
)
