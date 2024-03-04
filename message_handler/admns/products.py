from aiogram import Router
from aiogram.types import Message
from aiogram.filters import and_f
from aiogram.fsm.context import FSMContext
from data import sqlPrompts
import words
import filters
import keyboards
from . import add_product

router = Router()

@router.message(and_f(filters.admins.IsAdmin(), filters.any.textInTuple("Mahsulotlar", "Продукты", "Ónimler")))
async def manage_products_answer(message: Message):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    text = words.dict[lan]["manage_products"]["main_text"]
    await message.answer(text, reply_markup=keyboards.reply.products.manage_products_builder(lan))

