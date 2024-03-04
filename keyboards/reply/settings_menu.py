from aiogram.utils.keyboard import ReplyKeyboardBuilder
import words

def menu_builder(lan):
    builder = ReplyKeyboardBuilder()
    for i in words.dict[lan]["settings"]["main_menu"]:
        builder.button(text=i)
    builder.adjust(1)
    builder = builder.as_markup()
    builder.resize_keyboard = True
    return builder

def admin_menu_builder(lan):
    builder = ReplyKeyboardBuilder()
    for i in words.dict[lan]["settings"]["admin_menu"]:
        builder.button(text=i)
    builder.adjust(1)
    builder = builder.as_markup()
    builder.resize_keyboard = True
    return builder