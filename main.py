import datetime
from pprint import pprint
import requests
from config import apiKey


def get_weather(city, apiKey):
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
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}&units=metric")
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
        sunrice_timestamp = datetime.datetime.fromtimestamp (data["sys"]["sunrise"])
        sunset_timestamp = datetime.datetime.fromtimestamp (data["sys"]["sunset"])
        length_of_the_day = datetime.datetime.fromtimestamp(data["sys"]["sunset"]) - datetime.datetime.fromtimestamp(
            data["sys"]["sunrise"])

        print(f"***{datetime.datetime.now().strftime('%Y -%m-%d %H:%M')}***\n"
              f"Погода в місті:K {city}\nТемпература: {cur_weather}C°{wd}\n"
              f"Вологість: {cur_humidity}%\nТиск:{pressure}\nВітер:{wind}м/с\n"
              f"Схід сонця:{sunrice_timestamp}\nЗахід сонця:{sunset_timestamp}\nТривалість дня:{length_of_the_day}\n")

    except Exception as ex:
        print(ex)
        print("Перевірте назву міста")

def main():
    city = input("Вкажіть місто :")
    get_weather(city, apiKey)

if __name__ == '__main__':
    main()