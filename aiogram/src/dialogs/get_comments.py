from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.kbd import Row, Button
from aiogram_dialog.widgets.text import Format
from aiogram_dialog.widgets.text import Const

from states.comments import GetCommentsSG
from handlers.get_comments import show_comment, next_comment, prev_comment, back_to_menu

get_comments_dialog = Dialog(
    Window(
        Format("{comment}"),
        Row(
            Button(Const("⬅️"), id="prev_comment", on_click=prev_comment),
            Button(Const("Меню"), id="back_to_menu", on_click=back_to_menu),
            Button(Const("➡️"), id="next_comment", on_click=next_comment),
        ),
        state=GetCommentsSG.showing_comments,
        getter=show_comment,
    )
)
