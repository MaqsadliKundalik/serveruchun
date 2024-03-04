from aiogram.types import CallbackQuery
from aiogram import Bot, Router, F
from aiogram.fsm.context import FSMContext
import words
from data import sqlPrompts
from states import registration_state
from keyboards.reply import main_menu

router = Router()

@router.callback_query(registration_state.UserRegistration.lan)
async def user_registration_lan_answer(callback: CallbackQuery, state: FSMContext):
    lan = callback.data.split(":")[1]
    sqlPrompts.change_user_lan(callback.from_user.id, lan)
    await state.update_data(lan=lan)
    text = words.dict[lan]["sign up"]['lan']
    await callback.message.answer(text=text)
    await state.set_state(registration_state.UserRegistration.name)

@router.callback_query(F.data.startswith("confirmUser"))
async def user_change_status_answer(callback: CallbackQuery, bot: Bot):
    status = callback.data.split(":")[1]
    user_id = int(callback.data.split(":")[2])
    if sqlPrompts.get_user(int(user_id)):
        sqlPrompts.change_user_status(user_id, status)
        if status == "member":
            # try:
                print(sqlPrompts.get_user(user_id), user_id)
                lan = sqlPrompts.get_user(user_id)[1]
                text = words.dict[lan]["sign up"]["user_status_change_to_member_user_message"]
                await bot.send_message(user_id, text)

                text = words.dict[lan]["main_menu"]["text"]
                await bot.send_message(user_id, text=text, reply_markup=main_menu.menu_builder(lan))
                
                lan = sqlPrompts.get_user(callback.from_user.id)[1]
                text = words.dict[lan]["sign up"]["user_status_change_to_member_admin_message"]
                await callback.answer(text, show_alert=True)
                await callback.message.edit_text(callback.message.text + "\n\n<b>✅ Foydalanuvchi profili tasdiqlandi!</b>")
            # except:
            #     lan = sqlPrompts.get_user(callback.from_user.id)[1]
            #     sqlPrompts.del_user(user_id)
            #     text = words.dict[lan]["sign up"]["bug"]
            #     await callback.answer(text, show_alert=True)

        elif status == "none":
            try:
                lan = sqlPrompts.get_user(user_id)[1]
                text = words.dict[lan]["sign up"]["user_status_change_to_none_user_message"]
                await bot.send_message(user_id, text)

                lan = sqlPrompts.get_user(callback.from_user.id)[1]
                text = words.dict[lan]["sign up"]["user_status_change_to_none_admin_message"]
                await callback.answer(text, show_alert=True)    
            except:
                lan = sqlPrompts.get_user(callback.from_user.id)[1]
                sqlPrompts.del_user(user_id)
                text = words.dict[lan]["sign up"]["bug"]
                await callback.answer(text, show_alert=True)

    else:
        lan = sqlPrompts.get_user(callback.from_user.id)[1]
        text = words.dict[lan]["sign up"]["old_message"]
        
        await callback.answer(text, show_alert=True)
