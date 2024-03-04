from aiogram.utils.keyboard import ReplyKeyboardBuilder
import words

def menu_builder(lan):
    builder = ReplyKeyboardBuilder()
    for i in words.dict[lan]["main_menu"]["menu"]:
        builder.button(text=i)
    builder.adjust(2)
    return builder.as_markup()
