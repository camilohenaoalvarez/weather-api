from typing import Annotated

from fastapi import FastAPI, Query, HTTPException, status, Request
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware

from api.controllers.processor import create_instance

"""
    ## CODE FILE INFO:
    
    This is the main code file. Here you will find:
    - CORS setted up and 'allow origins' listed
    - Server api GET http method declaration (FastApi library used)
    - get_weather is an async function that has two parameters: city and country.
      both are strings and eachone has its own validation for the incoming data from the request
    - City parameter validatons: only strings with letters and spaces are accepted
    - Country parameter validatons: only strings with two letters
    - Finally it will create and prepare the weather object to be returned with the content-type header (application/json)
"""

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)



@app.get("/weather")
async def get_weather(
    city: Annotated[str, Query(regex="^[A-Za-z ]+$")] = ...,
    country: Annotated[str, Query(min_length=2, max_length=2, regex="^[a-z]+$")] = ...
):
    headers = {"Content-Type": "application/json"}
    
    try:
        weather_object = await create_instance(city, country)

        return JSONResponse(content = weather_object.get_weather_object(), headers = headers)
    
    except (Exception, HTTPException) as err:
        print('ERROR: ', err)
        return JSONResponse(content = {'Error ': str(err)}, status_code = status.HTTP_404_NOT_FOUND, headers = headers)
    
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    exc_str = f' {exc}'.replace('\n', ' ').replace('   ', ' ')

    if 'city string' in  exc_str:
        exc_str = 'please enter a valid city name'
    if 'country ensure' in exc_str:
        exc_str = 'please enter a valid country iso_2 code, ensure this value has at most 2 letters'

    return JSONResponse(
        content = {'Error ': exc_str},
        status_code = status.HTTP_422_UNPROCESSABLE_ENTITY,
        headers = {"Content-Type": "application/json"}
    )