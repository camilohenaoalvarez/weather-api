from datetime import datetime
import pytest

from api import utilities


@pytest.fixture
def input_values_for_utilities():
    return {
        "city": "cali",
        "country_iso2": "co",
        "name": "Santiago de Cali",
        "country": "CO",
        "celcius_temperature": 33,
        "fahrenheit_temperature": 91.4,
        "wind_speed": 1.54,
        "wind_speed_description": "light air",
        "wind_direction": 0,
        "wind_direction_description": "north",
        "cloudiness": "few clouds",
        "pressure": 1010,
        "humidity": 33,
        "timezone": -18000,
        "sunrise": "05:57",
        "sunset": "18:16",
        "latitude": 3.4372,
        "longitude": -76.5225,
        "requested_time": "2023-06-19 16:21:25",
        "location_name": "Santiago de Cali, CO",
        "temperature": {"celsius": "33 °C", "fahrenheit": "91.4 °F"},
        "wind": "light air, 1.54 m/s, north",
        "geo_coordinates": [3.4372, -76.5225],
    }

def test_convert_celcius_to_fahrenheit(input_values_for_utilities):
    celcius = input_values_for_utilities['celcius_temperature']
    assert input_values_for_utilities['fahrenheit_temperature'] == utilities.convert_celcius_to_fahrenheit(celcius)

def test_convert_wind_direction_deg_to_text(input_values_for_utilities):
    wind_direction_degs = input_values_for_utilities['wind_direction']
    assert input_values_for_utilities['wind_direction_description'] == utilities.convert_wind_direction_deg_to_text(wind_direction_degs)
    assert 'east-southeast' == utilities.convert_wind_direction_deg_to_text(110)
    assert 'east-southeast' == utilities.convert_wind_direction_deg_to_text(-110)

def test_get_wind_speed_description(input_values_for_utilities):
    wind_speed = input_values_for_utilities['wind_speed']
    assert input_values_for_utilities['wind_speed_description'] == utilities.get_wind_speed_description(wind_speed)
    assert 'strong gale' == utilities.get_wind_speed_description(21.99999999)
    assert 'strong breeze' == utilities.get_wind_speed_description(13.82222222)
    assert 'hurricane' == utilities.get_wind_speed_description(35.1)
    assert 'not description found for this speed value: -1 m/s' == utilities.get_wind_speed_description(-1)

def test_get_localized_human_time_from_unix():
    waalre_nl = {
        'human_sunrise': '05:21',
        'human_sunset': '21:58',
        'sunrise': 1687231275,
        'sunset': 1687291087,
        'timezone_in_seconds': 7200
    }

    curitiba_br = {
        'human_sunrise': '07:02',
        'human_sunset': '17:34',
        'sunrise': 1687168924,
        'sunset': 1687206890,
        'timezone_in_seconds': -10800
    }

    seoul_kr = {
        'human_sunrise': '05:10',
        'human_sunset': '19:56',
        'sunrise': 1687205444,
        'sunset': 1687258574,
        'timezone_in_seconds': 32400
    }

    assert waalre_nl['human_sunrise'] == utilities.get_localized_human_time_from_unix(
        waalre_nl['sunrise'],
        waalre_nl['timezone_in_seconds']
    )

    assert waalre_nl['human_sunset'] == utilities.get_localized_human_time_from_unix(
        waalre_nl['sunset'],
        waalre_nl['timezone_in_seconds']
    )

    assert curitiba_br['human_sunrise'] == utilities.get_localized_human_time_from_unix(
        curitiba_br['sunrise'],
        curitiba_br['timezone_in_seconds']
    )

    assert curitiba_br['human_sunset'] == utilities.get_localized_human_time_from_unix(
        curitiba_br['sunset'],
        curitiba_br['timezone_in_seconds']
    )

    assert seoul_kr['human_sunrise'] == utilities.get_localized_human_time_from_unix(
        seoul_kr['sunrise'],
        seoul_kr['timezone_in_seconds']
    )

    assert seoul_kr['human_sunset'] == utilities.get_localized_human_time_from_unix(
        seoul_kr['sunset'],
        seoul_kr['timezone_in_seconds']
    )


