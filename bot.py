from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from test import predict

TOKEN = '1772811656:AAH_gGeNFdePLy7rRZLYMB_4nx0GLiyZ0nc'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Привет! \nНажми /recognition")


@dp.message_handler(content_types=['photo'])
async def handle_docs_photo(message):

    await message.photo[-1].download('test.jpg')
    animal = predict()
    await message.answer(animal)


if __name__ == '__main__':
    executor.start_polling(dp)