from aiogram.fsm.state import State, StatesGroup

class AddPorduct(StatesGroup):
    name = State()
    size = State()
    soni = State()
    price = State()
    img1 = State()
    img2 = State()
    img3 = State()
    img4 = State()
    img5 = State()
    confirm = State()

class DelProduct(StatesGroup):
    id = State()

class ChangeCountProduct(StatesGroup):
    id = State()
    soni = State()