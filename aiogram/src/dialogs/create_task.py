from aiogram_dialog import Dialog, Window
from aiogram_dialog.widgets.input import TextInput
from aiogram_dialog.widgets.kbd import Row, Button, Multiselect
from aiogram_dialog.widgets.text import Const, Format

from getters import tasks
from handlers.create_task import confirm_task
from states.tasks import CreateTaskSG


create_task_dialog = Dialog(
    Window(
        Const("Введите заголовок задачи:"),
        TextInput(id="title", on_success=tasks.get_title),
        state=CreateTaskSG.waiting_for_title,
        getter=tasks.get_dialog_data,
    ),
    Window(
        Const("Введите описание задачи:"),
        TextInput(id="description", on_success=tasks.get_description),
        state=CreateTaskSG.waiting_for_description,
        getter=tasks.get_dialog_data,
    ),
    Window(
        Const("Введите дату выполнения задачи (YYYY-MM-DD):"),
        TextInput(id="due_date", on_success=tasks.get_due_date),
        state=CreateTaskSG.waiting_for_due_date,
        getter=tasks.get_dialog_data,
    ),
    Window(
        Const("Выберите категории задачи:"),
        Multiselect(
            Format("✓ {item[name]}"),
            Format("{item[name]}"),
            id="categories",
            item_id_getter=lambda x: x["name"],
            items="categories",
            on_state_changed=tasks.update_categories,
        ),
        Row(
            Button(
                Const("Добавить категорию"),
                id="add_category",
                on_click=lambda call, button, manager: manager.switch_to(CreateTaskSG.waiting_for_category_name)
            ),
            Button(Const(
                "Продолжить"),
                id="proceed",
                on_click=lambda call, button, manager: manager.switch_to(CreateTaskSG.waiting_for_confirmation)
            ),
        ),
        state=CreateTaskSG.waiting_for_categories,
        getter=tasks.get_categories
    ),
    Window(
        Const("Введите название новой категории:"),
        TextInput(id="category_name", on_success=tasks.save_category_name),
        state=CreateTaskSG.waiting_for_category_name,
    ),
    Window(
        Const("Подтвердите создание задачи:"),
        Row(
            Button(Const("Подтвердить"), id="confirm", on_click=confirm_task),
            Button(Const("Отменить"), id="cancel"),
        ),
        state=CreateTaskSG.waiting_for_confirmation,
    ),
)
