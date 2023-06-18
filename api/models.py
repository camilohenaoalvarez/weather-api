import asyncio
from typing import Sequence, Mapping
from datetime import datetime

from api.services.weather_api import rqeuest_weather
from api.utilities import convert_celcius_to_fahrenheit, \
    convert_wind_direction_deg_to_text as cwd, \
    get_wind_speed_description as gwsd, \
    get_localized_human_time_from_unix

class Location:
    def __init__(self, city:str, country_iso2:str):
        self.city:str = city
        self.country_iso2:str = country_iso2.lower()

class WeatherData(Location):
    location_name: str = None
    temperature: Mapping[str, str] = None
    wind: str = None
    cloudiness: str = None
    pressure: str = None
    humidity: str = None
    sunrise: str = None
    sunset: str = None
    geo_coordinates: Sequence[float]
    requested_time: str = None
    forecast: dict = None

    def __init__(self, city:str, country_iso2:str):
        super().__init__(city, country_iso2)

        print('... building object')
        self.set_weather_props()
        print('done!')

    def set_weather_props(self):
        data: dict =  asyncio.run(rqeuest_weather(self.city, self.country_iso2))

        self.location_name = f'{data.get("name")}, {data.get("sys").get("country")}'
        self.temperature = {
            'celsius': f'{data.get("main").get("temp")} °C',
            'fahrenheit': f'{convert_celcius_to_fahrenheit(data.get("main").get("temp"))} °F',
        }

        self.wind = f'{gwsd(data.get("wind").get("speed"))}, {data.get("wind").get("speed")} m/s, {cwd(data.get("wind").get("deg"))}'
        self.cloudiness = data.get("weather")[0].get("description")
        self.pressure = f'{data.get("main").get("pressure")} hPa'
        self.humidity = f'{data.get("main").get("humidity")} %'
        self.sunrise = get_localized_human_time_from_unix(data.get("sys").get("sunrise"), data.get("timezone"))
        self.sunset = get_localized_human_time_from_unix(data.get("sys").get("sunset"), data.get("timezone"))
        self.geo_coordinates = [data.get("coord").get("lat"), data.get("coord").get("lon")]
        self.requested_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.forecast = {}

    def get_weather_object(self):
        return {
            "location_name": self.location_name,
            "temperature": self.temperature,
            "wind": self.wind,
            "cloudiness": self.cloudiness,
            "pressure": self.pressure,
            "humidity": self.humidity,
            "sunrise": self.sunrise,
            "sunset": self.sunset,
            "geo_coordinates": self.geo_coordinates,
            "requested_time": self.requested_time,
            "forecast": self.forecast,
        }