from fastapi import FastAPI, Query
from typing import Annotated

from api.controllers.processor import create_instance

app = FastAPI()

@app.get("/")
async def get_weather(
    city: Annotated[str, Query(regex="^[A-Za-z ]+$")] = ...,
    country: Annotated[str, Query(min_length=2, max_length=2, regex="^[a-z]+$")] = ...
):
    try:
        weather_object = await create_instance(city, country)
        return weather_object.get_weather_object()
    
    except Exception as err:
        print('ERROR: ', err)
        return {'msg': str(err)}