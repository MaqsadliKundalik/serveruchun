from aiogram.utils.keyboard import ReplyKeyboardBuilder
import words
from data import sqlPrompts

def manage_menu_builder(lan):
    builder = ReplyKeyboardBuilder()
    for i in  words.dict[lan]["manage_users"]["main_menu"]:
        builder.button(text=i)
    builder.adjust(1)
    builder = builder.as_markup()
    builder.resize_keyboard = True
    return builder