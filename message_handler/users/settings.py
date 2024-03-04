from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from data import sqlPrompts
import filters
import words
import keyboards
import states

router = Router()

@router.message(filters.any.textInTuple("⚙️ Sozlamalar", "⚙️ Настройки", "⚙️ Sazlamalar"))
async def settings_answer(message: Message):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    text = words.dict[lan]["settings"]["main_text"]
    await message.answer(text, reply_markup=keyboards.reply.settings_menu.menu_builder(lan))

@router.message(filters.any.textInTuple("Tilni sozlash", "Языковые настройки", "Tildi sazlaw"))
async def settings_answer(message: Message, state: FSMContext):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    text = words.dict[lan]["settings"]["set_lan_text"]
    await message.answer(text, reply_markup=keyboards.inline.registration_menu.lan_builder)
    await state.set_state(states.set_lan.Set_lan.lan)

