import os
import aiohttp

from dotenv import load_dotenv

load_dotenv()

async def rqeuest_weather(city_name:str, country:str) -> dict:
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{country}&appid={os.getenv("WEATHER_API_KEY")}&units=metric'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print("request made to get weather data")
            return await resp.json()