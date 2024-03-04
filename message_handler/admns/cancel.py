from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import and_f
from data import sqlPrompts
import filters
import words
import keyboards

router = Router()

@router.message(and_f(filters.admins.IsAdmin(), filters.any.textInTuple("🚫 Bıykarlaw", "🚫 Отмена", "🚫 Bekor qilish")))
async def canceling_this_operation(message: Message, state:FSMContext):
    this_state = await state.get_state()
    if this_state: await state.clear()
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    await message.answer(message.text, reply_markup=keyboards.reply.admin_menu.main_menu_builder(lan))
