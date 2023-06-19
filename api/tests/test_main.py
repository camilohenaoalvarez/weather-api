from fastapi.testclient import TestClient
from jsonschema import validate
import jsonschema
import httpx
import json

from api.main import app

client = TestClient(app)

ok_response_schema = {
    "type" : "object",
    "properties" : {
        "location_name" : {"type" : "string"},
        "temperature" : {
            "type" : "object",
            "properties" : {
                "celsius" : {"type" : "string"},
                "fahrenheit" : {"type" : "string"},
            }
        },
        "wind" : {"type" : "string"},
        "cloudiness" : {"type" : "string"},
        "pressure" : {"type" : "string"},
        "humidity" : {"type" : "string"},
        "sunrise" : {"type" : "string"},
        "sunset" : {"type" : "string"},
        "geo_coordinates" : {"type" : "string"},
        "requested_time" : {"type" : "string"},
    },
}

def json_schema_validation(obj, schema):
    try:
        validate(instance = obj, schema = schema)
    except jsonschema.exceptions.ValidationError as err:
        print('Api response schema error: ', err)
        return False

    return True

def test_get_weather_with_valid_params():
    response = httpx.get("http://localhost:8000/weather", params={"city": "cali", "country":"co"})
    assert response.status_code == 200
    assert json_schema_validation(response.json(), ok_response_schema)


def test_get_weather_with_invalid_params():
    response = httpx.get("http://localhost:8000/weather", params={"city": "cali", "country":"nl"})
    assert response.status_code == 404
    assert response.json() == {"Error ":"Location not found. Please check the paremeters sent in the request"}

def test_not_valid_url():
    response = httpx.get("http://localhost:8000", params={"city": "cali", "country":"co"})
    assert response.status_code == 404
    assert response.json() == {"detail":"Not Found"}

def test_invalid_city():
    response = httpx.get("http://localhost:8000/weather", params={"city": "lima78", "country":"pe"})
    assert response.status_code == 404
    assert response.json() == {"Error ":"Location not found. Please check the paremeters sent in the request"}

def test_invalid_country():
    response = httpx.get("http://localhost:8000/weather", params={"city": "cali", "country":"col"})
    assert response.status_code == 422
    assert response.json() == {"Error ":"please enter a valid country iso_2 code, ensure this value has at most 2 letters"}