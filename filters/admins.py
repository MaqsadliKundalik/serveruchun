from aiogram.filters import Filter
from aiogram.types import Message
from data import sqlPrompts

class IsAdmin(Filter):
    async def __call__(self, message: Message):
        return bool(sqlPrompts.get_admin(message.from_user.id))
    