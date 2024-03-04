from typing import Any
from aiogram.filters import Filter
from aiogram.types import Message

class textInTuple(Filter):
    def __init__(self, *args):
        self.args = args

    async def __call__(self, message: Message):
        if message.text:
            self.args = [i.lower() for i in self.args]
            return message.text.lower() in self.args
        return False
