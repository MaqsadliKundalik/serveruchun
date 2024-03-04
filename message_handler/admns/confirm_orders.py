from aiogram import Router, F, Bot
from aiogram.types import Message, ReplyKeyboardRemove, FSInputFile
from aiogram.utils.media_group import MediaGroupBuilder
from aiogram.fsm.context import FSMContext
from aiogram.filters import and_f
from data import sqlPrompts
import keyboards
import words
import filters
import states
import utils

router = Router()

@router.message(and_f(filters.admins.IsAdmin(), filters.any.textInTuple("Buyurtmani ko'rish", "Посмотреть заказ", "Buyırtpanı kóriw")))
async def confirm_order_answer(message: Message, state: FSMContext):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    text = words.dict[lan]["confirm_order"]["in_text"]
    await message.answer(text, reply_markup=keyboards.reply.cancel.main_menu_builder(lan))
    await state.set_state(states.orders.ConfirmOrder.order_id)

@router.message(states.orders.ConfirmOrder.order_id)
async def confirm_order_id_answer(message: Message, bot: Bot, state: FSMContext):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    if message.text.isdigit():
        order_id = int(message.text)
        order = sqlPrompts.get_order_by_ID(order_id)
        if order:
            product = sqlPrompts.get_productById(order[1])
            sqlPrompts.change_order_status(order_id, "confirmed")
            text = words.dict[lan]["confirm_order"]["order_data"](product[0], product[2], order[2], order[2] * product[3], product[3], "⏳" if order[4] == "wait" else "❌" if order[4] == "rejected" else "✅")
            await message.answer(text, reply_markup=keyboards.inline.orders.confirm_order_builder(lan, order_id))
        else:
            text = words.dict[lan]["confirm_order"]["not_found_order"]
            await message.answer(text)
    else:
        text = words.dict[lan]["confirm_order"]["not_found_order"]
        await message.answer(text)

