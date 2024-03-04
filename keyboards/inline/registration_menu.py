from aiogram.utils.keyboard import InlineKeyboardBuilder

lan_builder = InlineKeyboardBuilder()
for i in ("UZ", "QA", "RU"):
    lan_builder.button(text=i, callback_data=f"changelan:{i}")
lan_builder = lan_builder.as_markup()

def admin_user_change_status_menu_builder(id):
    builder = InlineKeyboardBuilder()
    builder.button(text="✅ Tasdiqlash", callback_data=f"confirmUser:member:{id}")
    builder.button(text="❌ Rad etish", callback_data=f"confirmUser:none:{id}")
    return builder.as_markup()
