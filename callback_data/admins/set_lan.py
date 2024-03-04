from aiogram.types import CallbackQuery
from aiogram import Router
from data import sqlPrompts
import states
import words
import keyboards

router = Router()

@router.callback_query(states.set_lan.admin_set_lan.lan)
async def set_lan_answer(callback: CallbackQuery):
    lan = callback.data.split(":")[1]
    sqlPrompts.change_user_lan(callback.from_user.id, lan)

    text = words.dict[lan]["settings"]["changed_lan_text"]
    await callback.message.answer(text, reply_markup=keyboards.reply.admin_menu.main_menu_builder(lan))
