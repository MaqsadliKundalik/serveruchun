from aiogram.types import CallbackQuery
from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.filters import and_f
from data import sqlPrompts
import states
import words
import keyboards
import filters

router = Router()

@router.callback_query(and_f(filters.admins.IsAdmin(), F.data.startswith("changetime")))
async def set_time_answer(callback: CallbackQuery, state: FSMContext):
    lan = sqlPrompts.get_user(callback.from_user.id)[1]
    mil = callback.data.split(":")[1]
    vaqt = sqlPrompts.get_task_time()
    soat = vaqt[0]
    minut = vaqt[1]
    if mil == "hour":
        soat = callback.data.split(":")[2]
        await state.update_data(hour=soat)
        text = words.dict[lan]["settings"]["change_time_text"](str(soat).zfill(2), str(minut).zfill(2))
        await callback.message.edit_text(text, reply_markup=keyboards.inline.times.times_m_keyboard)

    if mil == "minute":
        data = await state.get_data()
        soat = data.get("hour")
        minut = callback.data.split(":")[2]
        text = words.dict[lan]["settings"]["change_time_text"](str(soat).zfill(2), str(minut).zfill(2))
        await callback.message.edit_text(text)
        await state.clear()
    sqlPrompts.change_task_time(soat, minut)

