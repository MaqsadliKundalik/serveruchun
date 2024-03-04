from aiogram.utils.keyboard import ReplyKeyboardBuilder
import words

def save_this_data_builder(lan):
    builder = ReplyKeyboardBuilder()
    for i in words.dict[lan]["add_product"]["send_imges_menu"]:
        builder.button(text=i)
    builder = builder.as_markup()
    builder.resize_keyboard = True
    builder.is_persistent = True
    return builder

def confirm_data_builder(lan):
    builder = ReplyKeyboardBuilder()
    for i in words.dict[lan]["add_product"]["confirm_data_menu"]:
        builder.button(text=i)
    builder = builder.as_markup()
    builder.resize_keyboard = True
    return builder
