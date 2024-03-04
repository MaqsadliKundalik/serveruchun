from typing import Any
from aiogram.filters import Filter
from aiogram.types import Message
from data import sqlPrompts

class IsUserInDB(Filter):
    async def __call__(self, message: Message):
        return not bool(sqlPrompts.get_user(message.from_user.id))

class IsUserInDBNot(Filter):
    async def __call__(self, message: Message):
        return sqlPrompts.get_user(message.from_user.id)[2] != "member"