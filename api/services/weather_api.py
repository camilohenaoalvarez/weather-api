import os
import aiohttp

from fastapi import HTTPException

from async_lru import alru_cache

from dotenv import load_dotenv

load_dotenv()

"""
    ## CODE FILE INFO:
    
    In the code below you will find:
    - Async request function to get the weather data to https://api.openweathermap.org api receiving the city and the country as parameters.
    - Once it has the data it will load the json response and will return a dictionary
    - LRU (least recently used) cache is used to cache data for 120 seconds
"""

@alru_cache(ttl=120)
async def rqeuest_weather(city_name:str, country:str) -> dict:
    url = f'{os.getenv("OPEN_WEATHER_API_URL")}?q={city_name},{country}&appid={os.getenv("WEATHER_API_KEY")}&units=metric'

    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            try:
                print("=" * 25,"http request made to Open Weather Map", "=" * 25)

                if resp.status == 404:
                    raise Exception('Location not found. Please check the paremeters sent in the request')
                
                return await resp.json()
            
            except Exception as err:
                print('Error: ', str(err))
                raise