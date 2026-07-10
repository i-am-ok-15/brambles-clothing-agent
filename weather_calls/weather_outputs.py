def simple_weather_print(forecast_tomorrow):
    for day in forecast_tomorrow:
        print(f"Time: {day['dt_txt']}")
        print(f"Feels like: {round(day['main']['feels_like'], 1)}°C")
        print(f"Probability of rain: {round(day['pop'] * 100)}%")
        print("====================================")
