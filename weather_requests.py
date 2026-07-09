import os
import requests
import json
from dotenv import load_dotenv
from datetime import date, timedelta

load_dotenv()
API_KEY = os.environ.get("OPENWEATHER_API_KEY")
FORECAST_LAT = os.environ.get("FORECAST_LAT")
FORECAST_LONG = os.environ.get("FORECAST_LONG")

# get weather forecast object from OpenWeather. Using 5 day, 3 hour increment forecast.
def get_forecast():
    forecast = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={FORECAST_LAT}&lon={FORECAST_LONG}&appid={API_KEY}&units=metric")
    return json.loads(forecast.content)

# strip out list of forecast increments and return as a list
def get_forecast_list(forecast_json):
    return forecast_json["list"]

# identify tomorrow's forecast items only and return increments betwene 0900 - 1800 hrs
def get_tomorrow_forecast(forecast_list):
    forecast_tomorrow = []
    for increment in forecast_list:
        date_time = increment["dt_txt"].split()
        yyyymmdd = date_time[0]
        hh = int(date_time[1].split(":")[0])
        tomorrow = str(date.today() + timedelta(days=1))
        if yyyymmdd == tomorrow:
            if hh >= 9 and hh <= 18:
                forecast_tomorrow.append(increment)
    return forecast_tomorrow


