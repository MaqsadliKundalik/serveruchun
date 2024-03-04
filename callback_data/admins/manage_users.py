from aiogram.types import CallbackQuery, ReplyKeyboardRemove
from aiogram import Bot, Router, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import and_f
import words
from data import sqlPrompts
import keyboards
import states
import asyncio

router = Router()

@router.callback_query(and_f(states.manage_users.ManageUsers.action, F.data.startswith("manageusers")))
async def manage_user_answer(callback: CallbackQuery):
    message = callback.message
    user_id = int(callback.data.split(":")[1])
    user = sqlPrompts.get_user(user_id)
    lan = sqlPrompts.get_user(callback.from_user.id)[1]
    if user:
        text = words.dict[lan]["manage_users"]["user_data"](user[0], user_id, user[3], user[2]) + "\n\n"
        text += words.dict[lan]["manage_users"]["manage_user_text"]
        await message.answer(text, reply_markup=keyboards.inline.manage_users.manage_user_menu(lan, user_id))
        await callback.message.delete()
    else:
        text = words.dict[lan]["manage_users"]["not_found_user"]
        await callback.answer(text)

@router.callback_query(and_f(states.manage_users.ManageUsers.action, F.data.startswith("manageuser")))
async def manage_user_command_answer(callback: CallbackQuery, bot: Bot, state: FSMContext):
    command = callback.data.split(":")[1]
    user_id = int(callback.data.split(":")[2])
    await state.update_data(user_id=user_id)
    lan = sqlPrompts.get_user(callback.from_user.id)[1]
    user = sqlPrompts.get_user(user_id)
    if command == "userslist":
        text = words.dict[lan]["manage_users"]["users_list_text"]
        await callback.message.answer(text, reply_markup=keyboards.inline.manage_users.users_list_menu_builder())
        await callback.message.delete()
        return 
    if user:
        user_lan = sqlPrompts.get_user(user_id)[1]
        if command == "delDB":
            sqlPrompts.del_user(user_id)
            user_alert_text = words.dict[user_lan]["manage_users"]["acc_alerts_for_user"]["del"]
            await bot.send_message(user_id, user_alert_text, reply_markup=ReplyKeyboardRemove())
            text = words.dict[lan]["manage_users"]["mission_acc"]
            await callback.answer(text, show_alert=True)
            
        elif command == "block":
            sqlPrompts.change_user_status(user_id, None)
            user_alert_text = words.dict[user_lan]["manage_users"]["acc_alerts_for_user"]["block"]
            await bot.send_message(user_id, user_alert_text, reply_markup=ReplyKeyboardRemove())
            text = words.dict[lan]["manage_users"]["mission_acc"]
            await callback.answer(text, show_alert=True)
        elif command == "active":
            sqlPrompts.change_user_status(user_id, "member")
            user_alert_text = words.dict[user_lan]["manage_users"]["acc_alerts_for_user"]["active"]
            await bot.send_message(user_id, user_alert_text, reply_markup=keyboards.reply.main_menu.menu_builder(user_lan))
            text = words.dict[lan]["manage_users"]["mission_acc"]
            await callback.answer(text, show_alert=True)
        elif command == "addadmin":
            if not sqlPrompts.get_admin(user_id):
                sqlPrompts.add_admin(user_id)
                user_alert_text = words.dict[user_lan]["manage_users"]["acc_alerts_for_user"]["addadmin"]
                await bot.send_message(user_id, user_alert_text, reply_markup=keyboards.reply.admin_menu.main_menu_builder(user_lan))

                text = words.dict[lan]["manage_users"]["mission_acc"]
                await callback.answer(text, show_alert=True)
            else:
                text = words.dict[lan]["manage_users"]["thisIsAdmin"]
                await callback.answer(text, show_alert=True)                

        elif command == "rmadmin":
            if sqlPrompts.get_admin(user_id):
                sqlPrompts.del_admin(user_id)
                user_alert_text = words.dict[user_lan]["manage_users"]["acc_alerts_for_user"]["rmAdmin"]
                await bot.send_message(user_id, user_alert_text, reply_markup=keyboards.reply.main_menu.menu_builder(user_lan))

                text = words.dict[lan]["manage_users"]["mission_acc"]
                await callback.answer(text, show_alert=True)
            else:
                text = words.dict[lan]["manage_users"]["thisIsNotAdmin"]
                await callback.answer(text, show_alert=True)
        elif command == "changebalans":
            await callback.message.answer(words.dict[lan]["manage_users"]["send_summa"])
            await state.set_state(states.manage_users.ManageUserBalans.balans)
            await callback.message.delete()
            return
        await callback.message.delete()
        
        user = sqlPrompts.get_user(user_id)
        text = words.dict[lan]["manage_users"]["user_data"](user[0], user_id, user[3], user[2]) + "\n\n"
        text += words.dict[lan]["manage_users"]["manage_user_text"]
        await callback.message.answer(text, reply_markup=keyboards.inline.manage_users.manage_user_menu(lan, user_id))
    else:
        text = words.dict[lan]["manage_users"]["not_found_user"]
        await callback.answer(text, show_alert=True)
        text = words.dict[lan]["manage_users"]["users_list_text"]
        await callback.message.answer(text, reply_markup=keyboards.inline.manage_users.users_list_menu_builder())
        await callback.message.delete()

