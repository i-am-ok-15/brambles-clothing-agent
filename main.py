import os
from dotenv import load_dotenv
from weather_requests import get_forecast, get_forecast_list, get_tomorrow_forecast
from weather_outputs import simple_weather_print
from weather_analysis import calculate_mean_temp, calculate_is_rainy
from clothing_selectors import get_clothing_options, select_headwear, select_bodywear, select_legwear, select_footwear, select_handwear, select_otherwear, select_bagwear

load_dotenv()
api_key = os.environ.get("OPENWEATHER_API_KEY")

def main():
    forecast_json = get_forecast()
    forecast_list = get_forecast_list(forecast_json)
    forecast_tomorrow = get_tomorrow_forecast(forecast_list)
    simple_weather_print(forecast_tomorrow)

    mean_temp = calculate_mean_temp(forecast_tomorrow)

    clothing_options = get_clothing_options()
    headwear = select_headwear(mean_temp, clothing_options)
    print(f"this is the headwear -> {headwear}")
    bodywear = select_bodywear(mean_temp, clothing_options)
    print(f"this is the headwear -> {bodywear}")
    legwear = select_legwear(mean_temp, clothing_options)
    print(f"this is the legwear -> {legwear}")
    footwear = select_footwear(mean_temp, clothing_options)
    print(f"this is the footwear -> {footwear}")
    handwear = select_handwear(mean_temp, clothing_options)
    print(f"this is the handwear -> {handwear}")
    otherwear = select_otherwear(mean_temp, clothing_options)
    print(f"this is the otherwear -> {otherwear}")
    bagwear = select_bagwear(mean_temp, clothing_options)
    print(f"this is the bagwear -> {bagwear}")

if __name__ == "__main__":
    main()
