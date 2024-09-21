from aiogram.fsm.state import StatesGroup, State


class GetTasksSG(StatesGroup):
    showing_task = State()


class CreateTaskSG(StatesGroup):
    waiting_for_title = State()
    waiting_for_description = State()
    waiting_for_due_date = State()
    waiting_for_categories = State()
    waiting_for_confirmation = State()
    waiting_for_category_name = State()


class CreateCommentSG(StatesGroup):
    waiting_for_comment = State()
    waiting_for_confirmation = State()
