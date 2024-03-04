from aiogram.utils.keyboard import ReplyKeyboardBuilder
import words


additional_items_uz = ReplyKeyboardBuilder()
for i in words.dict["UZ"]["additional_items"]["menu"]:
    additional_items_uz.button(text=i)
additional_items_uz.adjust(2)
additional_items_uz = additional_items_uz.as_markup()
additional_items_uz.resize_keyboard = True

additional_items_ru = ReplyKeyboardBuilder()
for i in words.dict["RU"]["additional_items"]["menu"]:
    additional_items_ru.button(text=i)
additional_items_ru.adjust(2)
additional_items_ru = additional_items_ru.as_markup()
additional_items_ru.resize_keyboard = True

additional_items_qa = ReplyKeyboardBuilder()
for i in words.dict["QA"]["additional_items"]["menu"]:
    additional_items_qa.button(text=i)
additional_items_qa.adjust(2)
additional_items_qa = additional_items_qa.as_markup()
additional_items_qa.resize_keyboard = True