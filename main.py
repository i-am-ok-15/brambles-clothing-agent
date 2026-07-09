import os
from dotenv import load_dotenv
from weather_requests import get_forecast, get_forecast_list, get_tomorrow_forecast
from weather_outputs import simple_weather_print

load_dotenv()
api_key = os.environ.get("OPENWEATHER_API_KEY")

def main():
    forecast_json = get_forecast()
    forecast_list = get_forecast_list(forecast_json)
    forecast_tomorrow = get_tomorrow_forecast(forecast_list)
    simple_weather_print(forecast_tomorrow)

if __name__ == "__main__":
    main()
