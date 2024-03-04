from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from aiogram import Bot, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import and_f
import words
from data import sqlPrompts
import keyboards
import states

router = Router()

@router.callback_query(and_f(states.orders.ConfirmOrder.order_id, F.data.startswith("confirmorder")))
async def manage_user_answer(callback: CallbackQuery, bot: Bot):
    message = callback.message
    command = callback.data.split(":")[1]
    order_id = int(callback.data.split(":")[2])
    order = sqlPrompts.get_order_by_ID(order_id)
    product = sqlPrompts.get_productById(order[1])
    user = sqlPrompts.get_user(order[0])
    lan = sqlPrompts.get_user(callback.from_user.id)[1]
    if user:
        if product:
            if order:
                status = ""
                if command == "confirmed":
                    sqlPrompts.change_order_status(order_id, "confirmed")
                    status = "confirmed"
                    text = words.dict[lan]["confirm_order"]["confirm_text"]
                    await message.answer(text)
                    await message.delete()

                elif command == "canceled":
                    sqlPrompts.change_order_status(order_id, "rejected")
                    sqlPrompts.change_user_balans(order[0], user[3] + product[3] * order[2])
                    sqlPrompts.update_product(order[2], soni=product[1] + order[2], is_soni=True)
                    status = "rejected"
                    text = words.dict[lan]["confirm_order"]["rejected_text"]
                    await message.answer(text)
                    await message.delete()
                text = words.dict[lan]["confirm_order"]["alert_order_user"](order_id, status)
                await bot.send_message(order[0], text)
            else:
                text = words.dict[lan]["confirm_order"]["not_found_order"]
                await message.answer(text)

        else:
            text = words.dict[lan]["confirm_order"]["not_found_product"]
            await message.answer(text)
            
    else:
        text = words.dict[lan]["confirm_order"]["not_found_user"]
        await message.answer(text)