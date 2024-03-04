from aiogram.utils.keyboard import ReplyKeyboardBuilder
import words

def orders_type_menu_builder(lan):
    builder = ReplyKeyboardBuilder()
    for i in words.dict[lan]["my_orders"]["main_menu"]:
        builder.button(text=i)
    builder.adjust(2)
    builder = builder.as_markup()
    builder.resize_keyboard = True
    return builder