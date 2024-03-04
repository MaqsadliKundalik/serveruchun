from aiogram import Router
from aiogram.filters import and_f
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from data import sqlPrompts
import filters
import words
import keyboards
import states

router = Router()

@router.message(and_f(filters.admins.IsAdmin(), filters.any.textInTuple("⚙️ Sozlamalar", "⚙️ Настройки", "⚙️ Sazlamalar")))
async def settings_answer(message: Message):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    text = words.dict[lan]["settings"]["main_text"]
    await message.answer(text, reply_markup=keyboards.reply.settings_menu.admin_menu_builder(lan))

@router.message(and_f(filters.admins.IsAdmin(), filters.any.textInTuple("Tilni sozlash", "Языковые настройки", "Tildi sazlaw")))
async def settings_answer(message: Message, state: FSMContext):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    text = words.dict[lan]["settings"]["set_lan_text"]
    await message.answer(text, reply_markup=keyboards.inline.registration_menu.lan_builder)
    await state.set_state(states.set_lan.admin_set_lan.lan)

@router.message(and_f(filters.admins.IsAdmin(), filters.any.textInTuple("Qarzdorlik bildirishnomasi vaqtini sozlash", "Настройка времени уведомления о задолженности", "Qarızdarlıq bildiriw xatı waqtın sazlaw")))
async def change_debtors_notlifaction_time_answer(message: Message, state: FSMContext):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    vaqt = sqlPrompts.get_task_time()
    text = words.dict[lan]["settings"]["change_time_text"](str(vaqt[0]).zfill(2), str(vaqt[1]).zfill(2))
    await message.answer(text, reply_markup=keyboards.inline.times.times_h_keyboard)

@router.message(and_f(filters.admins.IsAdmin(), filters.any.textInTuple("Qarzdorlik limitini sozlash", "Установка лимита долга", "Qarızdarlıq limitini sazlaw ")))
async def change_limit_answer(message: Message, state: FSMContext):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    limit = sqlPrompts.get_users_limit()[0]
    text = words.dict[lan]["settings"]["change_limit_text"](limit)
    await message.answer(text, reply_markup=keyboards.reply.cancel.cancel_menu_builder(lan))
    await state.set_state(states.set_limit.SetLimit.limit)

@router.message(and_f(states.set_limit.SetLimit.limit))
async def change_limit_limit_answer(message: Message, state: FSMContext):
    # try:
        lan = sqlPrompts.get_user(message.from_user.id)[1]
        limit = float(message.text)
        sqlPrompts.change_users_limit(limit)
        await message.answer("✅", reply_markup=keyboards.reply.admin_menu.main_menu_builder(lan))
        await state.clear()
    # except:
    #     await message.answer_sticker("CAACAgIAAxkBAAJEPWXkN7T5M3zuyFBmoRKeWOe6qT5-AAI5DwACdrIpSvr8TNGlMJ1aNAQ")
    