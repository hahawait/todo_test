from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Row, Button
from aiogram_dialog.widgets.text import Const

from getters.comments import get_comment
from handlers.create_comment import create_comment, confirm_comment
from states.comments import CreateCommentSG

create_comment_dialog = Dialog(
    Window(
        Const("Введите ваш комментарий:"),
        TextInput(id="comment", on_success=get_comment),
        state=CreateCommentSG.waiting_for_comment,
    ),
    Window(
        Const("Подтвердите создание комментария:"),
        Row(
            Button(Const("Подтвердить"), id="confirm", on_click=confirm_comment),
            Button(Const("Отменить"), id="cancel"),
        ),
        state=CreateCommentSG.waiting_for_confirmation,
    )
)
