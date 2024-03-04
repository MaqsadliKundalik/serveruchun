from aiogram.fsm.state import StatesGroup, State

class ManageUsers(StatesGroup):
    action = State()

class ManageUserBalans(StatesGroup):
    balans = State()

class SendMessageForUsers(StatesGroup):
    message = State()
