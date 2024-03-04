from aiogram.utils.keyboard import ReplyKeyboardBuilder

texts = "🚫 Bıykarlaw", "🚫 Отмена", "🚫 Bekor qilish"

def cancel_menu_builder(lan):
    builder = ReplyKeyboardBuilder()
    builder.button(text=texts[2 if lan == "UZ" else 1 if lan == "RU" else 0])
    builder = builder.as_markup()
    builder.resize_keyboard = True
    return builder

main_texts = ("🏠 Asosiy menyu", "🏠 Главное меню", "🏠 Tiykarǵı menyu")

def main_menu_builder(lan):
    builder = ReplyKeyboardBuilder()
    builder.button(text=main_texts[0 if lan == "UZ" else 1 if lan == "RU" else 2])
    builder = builder.as_markup()
    builder.resize_keyboard = True
    builder.is_persistent = True
    return builder

