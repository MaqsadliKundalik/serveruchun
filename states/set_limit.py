from aiogram.fsm.state import StatesGroup, State

class SetLimit(StatesGroup):
    limit = State()
    