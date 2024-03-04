from aiogram.fsm.state import State, StatesGroup

class UserGetPorduct(StatesGroup):
    name = State()
    soni = State()

class UserGetOerder(StatesGroup):
    name = State()

class ChangeOrderCount(StatesGroup):
    soni = State()

class GetFilteredOrders(StatesGroup):
    type = State()

class ConfirmOrder(StatesGroup):
    order_id = State()