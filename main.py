import os
from dotenv import load_dotenv
from weather_calls.weather_requests import get_forecast, get_forecast_list, get_tomorrow_forecast
from weather_calls.weather_outputs import simple_weather_print
from weather_calls.weather_analysis import calculate_mean_temp, calculate_is_rainy
from clothing_selectors import get_clothing_options, select_clothing
from ai_agent.ai_agent import ai_agent_call

load_dotenv()
api_key = os.environ.get("OPENWEATHER_API_KEY")

def main():
    forecast_json = get_forecast()
    forecast_list = get_forecast_list(forecast_json)
    forecast_tomorrow = get_tomorrow_forecast(forecast_list)
    simple_weather_print(forecast_tomorrow)

    mean_temp = calculate_mean_temp(forecast_tomorrow)

    clothing_options = get_clothing_options()
    clothing = select_clothing(mean_temp, clothing_options)
    ai_markdown = ai_agent_call(clothing, forecast_tomorrow)
    print(f"this is the ai_markfown\n {ai_markdown}")
    

if __name__ == "__main__":
    main()
