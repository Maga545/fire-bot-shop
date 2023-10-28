from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot= Bot('6804918347:AAHfhP5dwF56WzAaq04SGXG5unewWc8iaSo')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup =  types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть Магазин🛍', web_app=WebAppInfo(url='https://index-shop-fire-123.vercel.app/')))
    executor.start_polling(dp)
