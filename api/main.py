import asyncio
from fastapi import FastAPI, Query
from typing import Annotated

from cachetools import cached, TTLCache

from api.models import WeatherData

app = FastAPI()

# cache weather data for no longer than two minutes
@cached(cache=TTLCache(maxsize=10, ttl=120))
@app.get("/")
def get_weather(
    city: Annotated[str, Query(regex="^[A-Za-z]+$")] = ...,
    country: Annotated[str, Query(min_length=2, max_length=2, regex="^[A-Za-z]+$")] = ...
):
    
    weather_object = WeatherData(city, country).get_weather_object()
    
    return weather_object