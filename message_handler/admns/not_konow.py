from aiogram import Router
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import and_f
from data import sqlPrompts
import filters
import words
import keyboards

router = Router()

@router.message(filters.admins.IsAdmin())
async def not_know(message: Message, state: FSMContext):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    text = words.dict[lan]["not_know"]
    await message.answer(text)

