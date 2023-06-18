from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from typing import Annotated

from api.controllers.processor import create_instance

"""
    ## CODE FILE INFO:
    
    This is the main code file. Here you will find:
    - Server api GET http method declaration (FastApi library used)
    - get_weather is an async function that has two parameters: city and country.
      both are strings and eachone has its own validation for the incoming data from the request
    - City parameter validatons: only strings with letters and spaces are accepted
    - Country parameter validatons: only strings with two letters
    - Finally it will create and prepare the weather object to be returned with the content-type header (application/json)
"""

app = FastAPI()

@app.get("/")
async def get_weather(
    city: Annotated[str, Query(regex="^[A-Za-z ]+$")] = ...,
    country: Annotated[str, Query(min_length=2, max_length=2, regex="^[a-z]+$")] = ...
):
    headers = {"Content-Type": "application/json"}
    
    try:
        weather_object = await create_instance(city, country)

        return JSONResponse(content = weather_object.get_weather_object(), headers = headers)
        return weather_object.get_weather_object()
    
    except Exception as err:
        print('ERROR: ', err)
        return JSONResponse(content = {'msg': str(err)}, headers = headers)