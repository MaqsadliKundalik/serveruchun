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

@router.message(and_f(filters.admins.IsAdmin(), filters.any.textInTuple("Mahsulot miqdorini o'zgartirish", "Изменить количество товара", "Ónim muǵdarın ózgertiw")))
async def change_count_product_answer(message: Message, state: FSMContext):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    text = words.dict[lan]["change_count_product"]["input_text"]
    await message.answer(text, reply_markup=keyboards.reply.cancel.cancel_menu_builder(lan))
    await state.set_state(states.ProductsOperations.ChangeCountProduct.id)

@router.message(and_f(states.ProductsOperations.ChangeCountProduct.id, F.text))
async def del_product_name_answer(message: Message, bot: Bot, state:  FSMContext):
    if message.text.isdigit():
        product_id = message.text
        product = sqlPrompts.get_productById(product_id)
        lan = sqlPrompts.get_user(message.from_user.id)[1]
        if product:
            await state.update_data(name=product[0], size=product[2])
            text = words.dict[lan]["change_count_product"]["count_input_text"]
            await message.answer(text, reply_markup=ReplyKeyboardRemove())
            await state.set_state(states.ProductsOperations.ChangeCountProduct.soni)
        else:
            text = words.dict[lan]["change_count_product"]["not_find_product"]
            await message.answer(text)
    else:
        await message.answer("❌")

@router.message(states.ProductsOperations.ChangeCountProduct.soni)
async def change_count_product_answer(message: Message, state: FSMContext, bot: Bot):
    if message.text.isdigit():
        data = await state.get_data()
        product_name = data.get("name")
        product_size = data.get("size")
        product = sqlPrompts.get_product_by_name_and_size(product_name, product_size)
        lan = sqlPrompts.get_user(message.from_user.id)[1]
        if product and message.text.isdigit():
            text = words.dict[lan]["change_count_product"]["changed_count_product"]
            sqlPrompts.update_product(product[0], soni=product[1] + int(message.text), is_soni=True)
            await message.answer(text, reply_markup=keyboards.reply.admin_menu.main_menu_builder(lan))

            text_dict = {
                "msg1": words.dict["UZ"]["changed_count_product_message"](product_name, product_size),
                "msg2": words.dict["RU"]["changed_count_product_message"](product_name, product_size),
                "msg3": words.dict["QA"]["changed_count_product_message"](product_name, product_size)
            }
            sending_users = await utils.send_text_message_to_users(sqlPrompts.get_suers_id(), text_dict["msg1"], text_dict["msg2"], text_dict["msg3"], bot)
            text = words.dict[lan]["sending_message_users_count"](sending_users)
            await message.answer(text)
            await state.clear()
        
        elif not message.text.isdigit():
            text = words.dict[lan]["change_count_product"]["enter_an_integer"]
            await message.answer(text)
        else:
            text = words.dict[lan]["change_count_product"]["not_find_product"]
            await message.answer(text)
    else:
        await message.answer("❌")