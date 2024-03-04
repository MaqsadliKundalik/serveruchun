from aiogram import Bot, Dispatcher, Router, exceptions
from config import TOKEN, ADMIN_ID
from asyncio import run
from startup_and_shutdown import startup_answer, shutdown_answer
import callback_data
import message_handler

from aiogram.types import Message
from aiogram.filters import and_f, CommandStart
import filters.admins
from data import sqlPrompts
import words
import asyncio, datetime

dp = Dispatcher()



async def send_greeting():
    async def send_message(user_id: int, message: str, bot: Bot) -> bool:
        success = False
        flood = False
        try:
            await bot.send_message(chat_id=user_id, text=message)
            success = True
        except exceptions.TelegramRetryAfter as flood_error:
            await asyncio.sleep(flood_error.retry_after)
            flood = True
        finally:
            if flood:
                return await send_message(user_id, message)
            return success

    while True:
        vaqt = sqlPrompts.get_task_time()
        soat, minut = int(vaqt[0]), int(vaqt[1])
        soat += 5
        now = datetime.datetime.now()
        if now.hour == soat and now.minute == minut:
            for user in sqlPrompts.get_debtors():
                lan = sqlPrompts.get_user(user[0])[1]
                text = words.dict[lan]["debtor_message"](user[1], user[3])
                await send_message(user[0], text, bot)
                
                await asyncio.sleep(0.5)
        await asyncio.sleep(60)
            
async def main():
    global bot
    bot = Bot(token=TOKEN, parse_mode="HTML")

    dp.startup.register(startup_answer)
    dp.shutdown.register(shutdown_answer)

    dp.include_routers(
            message_handler.router,
            callback_data.router
        )
    asyncio.create_task(send_greeting())

    await dp.start_polling(bot, polling_timeout=1)
run(main())