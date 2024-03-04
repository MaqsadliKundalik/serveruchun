from aiogram.fsm.state import State, StatesGroup

class UserRegistration(StatesGroup):
    lan = State()
    name = State()
