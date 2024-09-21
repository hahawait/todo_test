from aiogram_dialog import DialogManager

from clients.django import APIClient
from states.tasks import CreateTaskSG


async def get_categories(dialog_manager: DialogManager, **kwargs):
    categories = dialog_manager.start_data.get("categories", [])
    return {"categories": categories}


async def get_dialog_data(dialog_manager: DialogManager, **kwargs):
    return dialog_manager.dialog_data


async def get_title(event, widget, dialog_manager: DialogManager, *args):
    dialog_manager.dialog_data["title"] = event.text
    await dialog_manager.next()


async def get_description(event, widget, dialog_manager: DialogManager, *args):
    dialog_manager.dialog_data["description"] = event.text
    await dialog_manager.next()


async def get_due_date(event, widget, dialog_manager: DialogManager, *args):
    dialog_manager.dialog_data["due_date"] = event.text
    await dialog_manager.next()


async def update_categories(event, widget, dialog_manager: DialogManager, *args):
    categories_names = widget.get_checked()
    categories = [
        category["id"] for category in dialog_manager.start_data["categories"] if category["name"] in categories_names
    ]
    dialog_manager.dialog_data["categories"] = categories


async def save_category_name(event, widget, dialog_manager: DialogManager, *args):
    category_name = event.text
    api_client: APIClient = dialog_manager.middleware_data['api_client']
    new_category = await api_client.create_categories(category_name)

    dialog_manager.start_data["categories"].append(new_category)
    await dialog_manager.switch_to(CreateTaskSG.waiting_for_categories)
