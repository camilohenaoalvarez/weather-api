from datetime import datetime

from api.models import WeatherData
from api.services.weather_api import request_weather

# put alias to long name functions
from api.utilities import convert_celcius_to_fahrenheit as ccf, \
    convert_wind_direction_deg_to_text as cwd, \
    get_wind_speed_description as gwsd, \
    get_localized_human_time_from_unix as lhtu


"""
    ## CODE FILE INFO:

    In the code below you will find:
    - Async request for the weather data to https://api.openweathermap.org api sending the city and the country as arguments.
    - Finally a WeatherData type object is created and loaded with data.
"""

async def create_instance(city: str, country: str) -> WeatherData:
    try:
        requested_weather_data: dict = await request_weather(city, country)
    except Exception as err:
        print (f'Open Weather api is not available, please try again later ... <ERR: {err}>')
        raise

    try:
        location_weather_obj: WeatherData =  WeatherData(city, country)
        load_instance_attrs(location_weather_obj, requested_weather_data)
    except:
        raise

    return location_weather_obj

def load_instance_attrs(weather_obj: WeatherData, weather_api_data: dict):
    try:
        weather_obj.name = weather_api_data.get("name")
        weather_obj.country = weather_api_data.get("sys").get("country")
        weather_obj.celcius_temperature = weather_api_data.get("main").get("temp")
        weather_obj.fahrenheit_temperature = ccf(weather_api_data.get("main").get("temp"))
        weather_obj.wind_speed = weather_api_data.get("wind").get("speed")
        weather_obj.wind_speed_description = gwsd(weather_api_data.get("wind").get("speed"))
        weather_obj.wind_direction = weather_api_data.get("wind").get("deg")
        weather_obj.wind_direction_description = cwd(weather_api_data.get("wind").get("deg"))
        weather_obj.cloudiness = weather_api_data.get("weather")[0].get("description")
        weather_obj.pressure = weather_api_data.get("main").get("pressure")
        weather_obj.humidity = weather_api_data.get("main").get("humidity")
        weather_obj.timezone = weather_api_data.get("timezone")
        weather_obj.sunrise = lhtu(weather_api_data.get("sys").get("sunrise"), weather_obj.timezone)
        weather_obj.sunset = lhtu(weather_api_data.get("sys").get("sunset"), weather_obj.timezone)
        weather_obj.latitude = weather_api_data.get("coord").get("lat")
        weather_obj.longitude = weather_api_data.get("coord").get("lon")
        weather_obj.requested_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        weather_obj.set_location_name()
        weather_obj.set_temperature()
        weather_obj.set_wind()
        weather_obj.set_geo_coordinates()
    except:
        raise