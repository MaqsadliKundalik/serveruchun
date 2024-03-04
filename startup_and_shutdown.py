from aiogram import Bot
from config import ADMIN_ID

async def startup_answer(bot: Bot):
    await bot.send_message(ADMIN_ID, "<b> ✅ Bot ishga tushdi! </b>")

async def shutdown_answer(bot: Bot):
    await bot.send_message(ADMIN_ID, "<b> ❗ Bot ishdan to'xtadi! </b>")