from aiogram.utils.keyboard import InlineKeyboardBuilder

times_h_keyboard = InlineKeyboardBuilder()
for i in range(1, 25):
    times_h_keyboard.button(text=str(i).zfill(2), callback_data=f"changetime:hour:{i}")
times_h_keyboard.adjust(4)
times_h_keyboard = times_h_keyboard.as_markup()

times_m_keyboard = InlineKeyboardBuilder()
for i in range(60):
    times_m_keyboard.button(text=str(i).zfill(2), callback_data=f"changetime:minute:{i}")
times_m_keyboard.adjust(6)
times_m_keyboard = times_m_keyboard.as_markup()