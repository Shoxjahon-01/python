import logging
import requests

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6163760030:AAEHbNhawXIDSQsKZQx-R71-IygLMSnV1Hk'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")



@dp.message_handler()
async def echo(message: types.Message):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid=8d36285f2c2c34d84ccc5a02a469195a')
    data = response.json()
    temp_celsium = data['main']['temp']-273.15
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    long =data['coord']['lon']
    lat = data['coord']['lat']
    answer_text =f'''
    Shaxar:{message.text}
    Harrorat:{temp_celsium}
    namlik:{humidity}
    Shamol tezligi:{wind_speed}
    kenglig:{long}
    Uzunliki:{lat}
    '''

    await message.answer(answer_text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)