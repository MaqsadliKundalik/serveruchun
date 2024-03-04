from aiogram import Router, F, Bot
from aiogram.filters import and_f
from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from data import sqlPrompts
from aiogram.fsm.context import FSMContext
import words
import states
import keyboards

router = Router()

@router.callback_query(and_f(states.orders.UserGetPorduct.name, F.data.startswith("addOrder")))
async def add_order_answer(callback: CallbackQuery, state: FSMContext):
    message = callback.message
    product_id = int(callback.data.split(":")[1])
    context_data = await state.get_data()
    lan = sqlPrompts.get_user(callback.from_user.id)[1]
    if product_id == context_data.get("id"):
        text = words.dict[lan]["products_user"]["send_order_soni"]
        await message.answer(text)    
        await state.set_state(states.orders.UserGetPorduct.soni)

@router.callback_query(and_f(states.orders.UserGetOerder.name, F.data.startswith("manageOrder")))
async def manage_order(callback: CallbackQuery, bot: Bot, state: FSMContext):
    message = callback.message
    command = callback.data.split(":")[1]
    order_id = int(callback.data.split(":")[2])
    lan = sqlPrompts.get_user(callback.from_user.id)[1]
    if command == "changeson":
        await state.update_data(order_id=order_id)
        text = words.dict[lan]["basket"]["send_order_count"]
        await message.answer(text)
        await state.set_state(states.orders.ChangeOrderCount.soni)
    elif command == "delorder":
        sqlPrompts.del_order(order_id)

        for i in sqlPrompts.get_admins():
            lan = sqlPrompts.get_user(i[0])[1]
            user = sqlPrompts.get_user(callback.from_user.id)
            text = words.dict[lan]["deleted_order_message"](order_id, user[0])
            await bot.send_message(chat_id=i[0], text=text)
        
        text = words.dict[lan]["basket"]["deleted_order"]
        await message.answer(text, reply_markup=keyboards.reply.main_menu.menu_builder(lan))    
        await state.clear()
    await callback.answer()
    
        