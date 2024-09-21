from aiogram.fsm.state import StatesGroup, State


class RegistrationSG(StatesGroup):
    waiting_for_password = State()
