from aiogram import Router, F, Bot
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.filters import and_f
from data import sqlPrompts
import keyboards
import words
import filters
import states
import utils

router = Router()

@router.message(and_f(filters.admins.IsAdmin(), filters.any.textInTuple("Mahsulot o'chirish", "Удаление продукта", "Ónim óshiriw")))
async def del_product_answer(message: Message, state: FSMContext):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    text = words.dict[lan]["del_product"]["input_text"]
    await message.answer(text, reply_markup=keyboards.reply.cancel.cancel_menu_builder(lan))
    await state.set_state(states.ProductsOperations.DelProduct.id)

@router.message(and_f(states.ProductsOperations.DelProduct.id, F.text))
async def del_product_name_answer(message: Message, bot: Bot, state:  FSMContext):
    if message.text.isdigit():
        product_id = int(message.text)
        product = sqlPrompts.get_productById(product_id)
        lan = sqlPrompts.get_user(message.from_user.id)[1]
        if product:
            text = words.dict[lan]["del_product"]["deleted_product"]
            sqlPrompts.delete_product(product_id)
            await message.answer(text, reply_markup=keyboards.reply.admin_menu.main_menu_builder(lan))

            text_dict = {
                "msg1": words.dict["UZ"]["deleted_product_message"](product[0], product[2]),
                "msg2": words.dict["RU"]["deleted_product_message"](product[0], product[2]),
                "msg3": words.dict["QA"]["deleted_product_message"](product[0], product[2])
            }
            sending_users = await utils.send_text_message_to_users(sqlPrompts.get_suers_id(), text_dict["msg1"], text_dict["msg2"], text_dict["msg3"], bot)
            text = words.dict[lan]["sending_message_users_count"](sending_users)
            await message.answer(text)
            await state.clear()
        else:
            text = words.dict[lan]["del_product"]["not_find_product"]
            await message.answer(text)
    else:
        await message.answer("❌")
