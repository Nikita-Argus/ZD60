from aiogram import Dispatcher, Bot, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage

API ='7667344013:AAGJcxthiQpVT4A97IyHNBCSrJccmybeHnk'
BOT_NAME = 'VoltDandadanbot'

def print_hi(name):
    print(f'Hi, {name}')
bot = Bot(token=API)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

if __name__ == '__main__':
    print_hi('PyCharm')

@dp.message_handler()
async def all_massages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)