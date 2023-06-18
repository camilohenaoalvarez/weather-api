from typing import Sequence, Mapping
from abc import ABC

"""
    ## CODE FILE INFO:
    
    Two models - classes were created:
    - 1. the abstract Location class that represents de entity, just declaring its attributes and types
    - 2. the WeatherData class that is an inheritation from Location class

    - WeatherData class has the methods and the structure to prepare its instances for the outside format.
"""

class Location(ABC):
    name: str = None
    country: str = None
    celcius_temperature: float = None
    fahrenheit_temperature: float = None
    wind_speed: float = None
    wind_speed_description: str = None
    wind_direction: int = None
    wind_direction_description: str = None
    cloudiness: str = None
    pressure: float = None
    humidity: float = None
    timezone: int = None
    sunrise: str = None
    sunset: str = None
    latitude: float = None
    longitude: float = None
    forecast: dict = {}

    def __init__(self, city:str, country_iso2:str):
        self.city:str = city
        self.country_iso2:str = country_iso2

class WeatherData(Location):
    location_name: str = None
    temperature: Mapping[str, str] = None
    wind: str = None
    geo_coordinates: Sequence[float]
    requested_time: str = None

    def __init__(self, city:str, country_iso2:str):
        super().__init__(city, country_iso2)

    def set_location_name(self):
        if not self.name or not self.country:
            raise ValueError("name or country values must have been defined")
        
        self.location_name = f'{self.name}, {self.country}'

    def set_temperature(self):
        if not self.celcius_temperature or not self.fahrenheit_temperature:
            raise ValueError("celcius or fahrenheit temperature values must have been defined")

        self.temperature = {
            'celsius': f'{self.celcius_temperature} °C',
            'fahrenheit': f'{self.fahrenheit_temperature} °F',
        }
    
    def set_wind(self):
        if not self.wind_speed_description or not self.wind_speed or not self.wind_direction_description:
            raise ValueError("wind values must have been defined")
        
        f'{self.wind_speed_description}, {self.wind_speed} m/s, {self.wind_direction_description}'

    def set_geo_coordinates(self):
        if not self.celcius_temperature or not self.fahrenheit_temperature:
            raise ValueError("latitude or longitude coordinates must have been defined")
        
        self.geo_coordinates = [self.latitude, self.longitude]

    def get_weather_object(self):
        return {
            "location_name": self.location_name,
            "temperature": self.temperature,
            "wind": self.wind,
            "cloudiness": self.cloudiness,
            "pressure": f'{self.pressure} hPa',
            "humidity": f'{self.humidity} %',
            "sunrise": self.sunrise,
            "sunset": self.sunset,
            "geo_coordinates": str(self.geo_coordinates),
            "requested_time": self.requested_time,
            "forecast": self.forecast,
        }