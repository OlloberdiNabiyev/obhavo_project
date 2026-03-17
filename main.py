import requests
import time
import asyncio
from aiohttp import ClientSession
from watchfiles import awatch
from Api import API_key

API_key = API_key
URL = "https://api.openweathermap.org/data/2.5/weather"

async def weather(city_name):
    parametrs = {
        "q": city_name,
        "appid": API_key,
        "units": 'metric'
    }
    try:

        async with ClientSession() as session:
           async with session.get(URL, params=parametrs) as response:
                data = await response.json()
                temp = data['main']['temp']
                return f"{city_name.title()} shahrida harorat {temp} gradus selsiy."
    except Exception as e:
        return f"{city_name} topilmadi {e}"


cities = [
    'Istanbul',
    'Mecca',
    'Madinah',
    'Jakarta',
    'Tehran',
    'Baghdad',
    'Cairo',
    'Riyadh',
    'Dubai',
    'Kuala Lumpur',
    'Lahore',
    'Dhaka',
    'Casablanca',
    'Algiers',
    'Damascus',
    'Amman',
    'Kuwait City',
    'Doha',
    'Manama',
    'Muscat'
]

start = time.time()
async def main(city_name):
    task_weather = []
    for city in cities:
        task = asyncio.create_task(weather(city))
        task_weather.append(task)

    for task in task_weather:
        res = await task
        print(res)

asyncio.run(main(cities))

end_time = time.time()
print(f"\n{end_time - start, 4} soniya vaqt ketdi")