# import time
# import asyncio
#
#
# async def generate_number():
#     for i in range(1, 11):
#         print(i)
#         await asyncio.sleep(1)
#
# async def say_message():
#     print("Asinxrom ishladi")
#
# async def main():
#     task1 = asyncio.create_task(generate_number())
#     task2 = asyncio.create_task(say_message())
#
#     await   task1
#     await task2
#
#     # task1 =  generate_number()
#     # task2 =  say_message()
#
#     await asyncio.gather(task1, task2)
#
# asyncio.run(main())

## --------------------------------------
import requests
import time
import asyncio
from aiohttp import ClientSession
from watchfiles import awatch

API_key = 'b01e7608c07f15c54ff9d9b64d478705'
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