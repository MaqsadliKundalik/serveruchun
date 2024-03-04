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

@router.message(and_f(filters.admins.IsAdmin(), filters.any.textInTuple("Foydalanuvchilar", "Пользователи", "Paydalanıwshılar")))
async def users_answer(message: Message, state: FSMContext):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    text = words.dict[lan]["manage_users"]["main_text"]
    await message.answer(text, reply_markup=keyboards.reply.manage_users.manage_menu_builder(lan))
    await state.set_state(states.manage_users.ManageUsers.action)

@router.message(and_f(states.manage_users.ManageUsers.action, filters.any.textInTuple("Foydalanuvchilar ro'yhati", "Список пользователей", "Paydalanıwshılar kestesi")))
async def manage_users_action_answer(message: Message, state: FSMContext):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    text = words.dict[lan]["manage_users"]["users_list_text"]
    wait_message = await message.answer("...", reply_markup=keyboards.reply.cancel.cancel_menu_builder(lan))
    await message.answer(text, reply_markup=keyboards.inline.manage_users.users_list_menu_builder())

@router.message(and_f(states.manage_users.ManageUsers.action, filters.any.textInTuple("Xabar yuborish", "Отправить сообщение", "Xabar jiberiw")))
async def send_message_for_users_answer(message: Message, state: FSMContext):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    text = words.dict[lan]["manage_users"]["input_message_text"]
    await message.answer(text, reply_markup=keyboards.reply.cancel.cancel_menu_builder(lan))
    await state.set_state(states.manage_users.SendMessageForUsers.message)

@router.message(states.manage_users.SendMessageForUsers.message)
async def send_message_users_message_answer(message: Message, state: FSMContext):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    text = words.dict[lan]["manage_users"]["acc_message"]
    await message.answer(text, reply_markup=keyboards.reply.admin_menu.main_menu_builder(lan))
    sending_users = await utils.send_message_to_users(sqlPrompts.get_suers_id(), message)
    text = words.dict[lan]["sending_message_users_count"](sending_users)
    await message.answer(text)
    await state.clear()
@router.message(states.manage_users.ManageUserBalans.balans)
async def sent_user_balans_answer(message: Message, bot: Bot, state: FSMContext):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    try:
        pul = float(message.text)
        data = await state.get_data()
        user_id = data.get("user_id")
        user = sqlPrompts.get_user(user_id)
        balans = user[3] + pul
        sqlPrompts.change_user_balans(user_id, balans)
        await message.answer("✅")
        await bot.send_message(user_id, f"➕ Balans: {utils.pulni_qismlash(balans)} UZS")
        user = sqlPrompts.get_user(user_id)
        text = words.dict[lan]["manage_users"]["user_data"](user[0], user_id, user[3], user[2]) + "\n\n"
        text += words.dict[lan]["manage_users"]["manage_user_text"]
        await message.answer(text, reply_markup=keyboards.inline.manage_users.manage_user_menu(lan, user_id))
        await state.set_state(states.manage_users.ManageUsers.action)
    except:
        await message.answer("🔢")
        