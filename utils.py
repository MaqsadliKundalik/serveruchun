from typing import List
from aiogram.types import Message
from aiogram import exceptions, Bot
from data import sqlPrompts
import asyncio


def open_tuple_in_list(lst: list):
    return [i[0] for i in lst]

async def send_message_to_users(all_users_id: List[int], sending_message: Message, sleep: float = 0.05) -> int:

    async def send_message(user_id: int, message: Message) -> bool:
        success = False
        flood = False
        try:
            await message.send_copy(chat_id=user_id)
            success = True
        except exceptions.TelegramRetryAfter as flood_error:
            await asyncio.sleep(flood_error.retry_after)
            flood = True
        finally:
            if flood:
                return await send_message(user_id, message)
            return success

    successfully_sent = 0
    for user in all_users_id:
        sent = await send_message(user, sending_message)
        if sent:
            successfully_sent += 1
        await asyncio.sleep(sleep)
    return successfully_sent

async def send_text_message_to_users(all_users_id: List[int], msg1 : str, msg2 : str, msg3 : str, bot: Bot,  sleep: float = 0.05) -> int:

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

    successfully_sent = 0
    for user in all_users_id:
        lan = sqlPrompts.get_user(user)[1]

        sent = False
        if lan == "UZ": sent = await send_message(user, msg1, bot)
        elif lan == "RU": sent = await send_message(user, msg2, bot)
        elif lan == "QA": sent = await send_message(user, msg3, bot)

        if sent:
            successfully_sent += 1
        await asyncio.sleep(sleep)
    return successfully_sent

def pulni_qismlash(son):
    return son
