from aiogram.fsm.state import StatesGroup, State


class CreateCommentSG(StatesGroup):
    waiting_for_comment = State()
    waiting_for_confirmation = State()


class GetCommentsSG(StatesGroup):
    showing_comments = State()
