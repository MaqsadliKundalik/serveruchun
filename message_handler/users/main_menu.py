from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from data import sqlPrompts
import filters
import words
import keyboards

router = Router()

@router.message(filters.any.textInTuple("🏠 Asosiy menyu", "🏠 Главное меню", "🏠 Tiykarǵı menyu"))
async def main_menu_answer(message: Message, state: FSMContext):
    this_state = await state.get_state()
    if this_state: await state.clear()
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    await message.answer(message.text, reply_markup=keyboards.reply.main_menu.menu_builder(lan))
