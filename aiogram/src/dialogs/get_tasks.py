from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Row, Button
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.text import Const

from states.tasks import GetTasksSG
from handlers.create_comment import create_comment
from handlers.get_comments import get_comments
from handlers.get_tasks import show_task, next_task, prev_task, back_to_menu

get_tasks_dialog = Dialog(
    Window(
        Format("{task}"),
        Row(
            Button(Const("⬅️"), id="prev_task", on_click=prev_task),
            Button(Const("Меню"), id="back_to_menu", on_click=back_to_menu),
            Button(Const("➡️"), id="next_task", on_click=next_task),
        ),
        Row(
            Button(Const("Добавить комментарий"), id="add_comment", on_click=create_comment),
        ),
        Row(
            Button(Const("Посмотреть комментарии"), id="get_comments", on_click=get_comments),
        ),
        state=GetTasksSG.showing_task,
        getter=show_task,
    )
)
