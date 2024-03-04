from aiogram import Bot, Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.filters import CommandStart, and_f
from keyboards.inline import registration_menu
from keyboards import reply
from states import registration_state
from data import sqlPrompts
import words
import filters
import keyboards

router = Router()

@router.message(and_f(CommandStart()))
async def user_start_answer(message: Message):
    lan = sqlPrompts.get_user(message.from_user.id)[1]
    text = words.dict[lan]["start"]["user"]
    await message.answer(text=text, reply_markup=reply.main_menu.menu_builder(lan))

@router.message(registration_state.UserRegistration.name)
async def user_registration_name_answer(message: Message, bot: Bot, state: FSMContext):
    data = await state.get_data()
    lan = data.get("lan")
    if (message.from_user.id, ) in sqlPrompts.get_admins():
        text = words.dict[lan]["start"]["admin"]
        sqlPrompts.change_user_name(message.from_user.id, message.text)
        await message.answer(text, reply_markup=keyboards.reply.admin_menu.main_menu_builder(lan))
    else:
        sqlPrompts.change_user_name(message.from_user.id, message.text)
        admin_message_text = f"<b>YANGI FOYDALANUVCHI:</b>\n<b>Ism-familya:</b> {message.text}\n<b>Tili:</b> {lan}"

        for admin_id in sqlPrompts.get_admins():
            await bot.send_message(admin_id[0], admin_message_text, reply_markup=registration_menu.admin_user_change_status_menu_builder(message.from_user.id))


        text = words.dict[lan]["sign up"]["name"]    

        await message.answer(text)
        await state.clear()


@router.message(filters.users.IsUserInDB())
async def user_registration_answer(message: Message, state: FSMContext):
    await message.answer("<b>UZ:</b> Tilingizni tanlang.\n<b>QA:</b> Tilińizdi saylań.\n<b>RU</b>Выберите ваш язык.", reply_markup=registration_menu.lan_builder)
    sqlPrompts.add_user(message.from_user.id, None, None)
    await state.set_state(registration_state.UserRegistration.lan)

@router.message(filters.users.IsUserInDBNot())
async def block_user_answmer(message: Message):
    text = ""
    for i in ("UZ", "RU", "QA"):
        text += words.dict[i]["block_user"] + "\n"
    await message.answer(text, reply_markup=ReplyKeyboardRemove())
