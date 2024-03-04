from aiogram.utils.keyboard import ReplyKeyboardBuilder
import words

def main_menu_builder(lan):
     builder = ReplyKeyboardBuilder()
     for i in words.dict[lan]["admin_menu"]:
         builder.button(text=i)
     builder.adjust(2)
     builder = builder.as_markup()
     builder.resize_keyboard = True
     builder.is_persistent = True
     return builder