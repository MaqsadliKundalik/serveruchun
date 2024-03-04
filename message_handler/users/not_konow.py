from aiogram import Router
from aiogram.types import Message
from data import sqlPrompts
import words

router = Router()

@router.message()
async def not_know(message: Message):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    text = words.dict[lan]["not_know"]
    await message.answer(text)

