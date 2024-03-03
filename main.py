from aiogram import Bot, Dispatcher, F
from aiogram.types import FSInputFile, Message
from asyncio import run

dp = Dispatcher()

async def get_db(message: Message):
    await message.answer_document(FSInputFile("data.db"))
async def set_db(message: Message, bot: Bot):
    file = await bot.get_file(message.document.file_id)
    await bot.download_file(file_path=file.file_path, destination=message.document.file_name)

    await message.answer("Yuklandi")
async def main():
    bot = Bot(token="6314941701:AAF-SMUQJGLWGNsh_B9bz_muiFRpaTBB4xQ")

    dp.message.register(get_db, F.text == "get")
    dp.message.register(set_db, F.document)

    await dp.start_polling(bot)
run(main())