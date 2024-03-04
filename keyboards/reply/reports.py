from aiogram.utils.keyboard import ReplyKeyboardBuilder
import words

def date_menu_builder(lan):
    builder = ReplyKeyboardBuilder()
    for i in words.dict[lan]["reports"]["main_menu"]:
        builder.button(text=i)
    builder.adjust(2)
    builder = builder.as_markup()
    builder.resize_keyboard = True
    return builder

def admin_menu_builder(lan):
    builder = ReplyKeyboardBuilder()
    for i in words.dict[lan]["reports"]["admin_menu"]:
        builder.button(text=i)
    builder.adjust(2)
    builder = builder.as_markup()
    builder.resize_keyboard = True
    return builder