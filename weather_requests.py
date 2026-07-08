import os
import requests
import json
from dotenv import load_dotenv
from config import FORECAST_LAT, FORECAST_LONG

load_dotenv()
API_KEY = os.environ.get("OPENWEATHER_API_KEY")

# waiting for api_key to be validated
# forecast = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={FORECAST_LAT}&lon={FORECAST_LONG}&appid={API_KEY}")
# print(forecast)

with open("test_json.json", "r") as f:
    forecast = json.load(f)
    list = forecast["list"]
    for day in list:
        print(f"Feels like: {round(day["main"]["feels_like"] - 273.15, 2)}°C")
        print(f"Probability of rain: {round(day["pop"] * 100)}%")
        print("====================================")