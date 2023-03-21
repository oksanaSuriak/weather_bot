import requests
import datetime

from aiogram.dispatcher import Dispatcher
from aiogram import Bot, types
from aiogram.utils import executor
import telebot


apiKey = "0c9aa0cd1afbf05191a808e0dbfd7f21"
tg_bot_token = "6282754646:AAEjcO8bEdYOeQwjH2JiQUnc7H3k7TEIdVM"


bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Привіт! Напиши назву міста і отримаєш прогноз погоди")



@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Хмарно \U00002601",
        "Rain": "Дощ \U00002614",
        "Drizzle": "Дощ \U00002600",
        "Thunderstorn": "Гроза \U000026A1",
        "Show": "Сніг \U0001F328",
        "Mist": "Туман \U0001F328"
    }

    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={apiKey}&units=metric")
        data = r.json()
        # pprint(data)
        city = data["name"]
        cur_weather = data["main"]["temp"]
        weather_description = data["weather"][0]["main"]
        if weather_description in code_to_smile:
            wd = code_to_smile[weather_description]
        else:
            wd = "Вигляни в вікно!"

        cur_humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrice_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp(data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        await message.reply(f"***{datetime.datetime.now().strftime('%Y -%m-%d %H:%M')}***\n"
              f"Погода в місті: {city}\nТемпература: {cur_weather}C°{wd}\n"
              f"Вологість: {cur_humidity}%\nТиск:{pressure}\nВітер:{wind}м/с\n"
              f"Схід сонця:{sunrice_timestamp}\nЗахід сонця:{sunset_timestamp}\nТривалість дня:{length_of_the_day}\n")

    except:
        await message.reply("\U00002620 Перевірте назву міста \U00002620")


if __name__ == '__main__':
    executor.start_polling(dp)
