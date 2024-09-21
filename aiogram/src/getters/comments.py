from aiogram_dialog import DialogManager


async def get_comment(event, widget, dialog_manager: DialogManager, *args):
    dialog_manager.dialog_data["comment"] = event.text
    await dialog_manager.next()
