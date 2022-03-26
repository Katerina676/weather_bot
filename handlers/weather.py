import requests
from config import weather_token
from aiogram import types
from dispatcher import dp


@dp.message_handler(commands=['start'])
async def start(msg: types.Message):
    await msg.answer(f'Привет {msg.from_user.first_name}, напиши название города')


@dp.message_handler()
async def get_weather(msg: types.Message):
    smiles = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Облачно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002614",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Снег \U0001F328",
        "Mist": "Туман \U0001F32B"
    }

    try:
        data = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={msg.text}&appid={weather_token}&units=metric")
        r = data.json()
        city = r['name']
        country = r['sys']['country']
        current_weather = r['main']['temp']
        weather_description = r['weather'][0]['main']
        if weather_description in smiles:
            wd = smiles[weather_description]
        else:
            wd = 'Посмотри в окно'
        pressure = r['main']['pressure']
        feels_like = r['main']['feels_like']
        wind = r['wind']['speed']
        await msg.answer(f'Город: {city}\nСтрана: {country}\nТемпература: {current_weather}C {wd}\n'
                f'Ощущается как: {feels_like}C\nДавление: {pressure}мм.рт.ст\n'
                f'Ветер: {wind}')

    except:
        await msg.answer('\U0001F648 Введите корректный город ')

