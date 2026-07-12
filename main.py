import os

from dotenv import load_dotenv

from ai_agent.ai_agent import ai_agent_call
from clothing_selectors import get_clothing_options, select_clothing
from ssg.src.ssg import ssg
from weather_calls.weather_analysis import calculate_mean_temp
from weather_calls.weather_outputs import simple_weather_print
from weather_calls.weather_requests import (
    get_forecast,
    get_forecast_list,
    get_tomorrow_forecast,
)

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

    with open("./ssg/src/content/index.md", "w", encoding="utf-8") as f:
        f.write(ai_markdown)
    ssg()


if __name__ == "__main__":
    main()
