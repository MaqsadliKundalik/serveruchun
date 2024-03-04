from aiogram.types import Message
from aiogram import Bot, Router
from aiogram.filters import CommandStart, and_f
from aiogram.fsm.context import FSMContext
from data import sqlPrompts
import words
import filters.admins
from ..users import start
import keyboards

router = Router(name="admins_start_router")


@router.message(filters.users.IsUserInDB())
async def user_registration_answer(message: Message, state: FSMContext):
    await start.user_registration_answer(message, state)

@router.message(and_f(filters.admins.IsAdmin(), CommandStart()))
async def start_command_answer(message: Message):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    text = words.dict[lan]["start"]["admin"]
    await message.answer(text, reply_markup=keyboards.reply.admin_menu.main_menu_builder(lan))
