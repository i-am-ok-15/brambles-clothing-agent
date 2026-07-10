def calculate_mean_temp(forecast_tomorrow: list) -> float:
    total_temp = 0
    for increment in forecast_tomorrow:
        total_temp += increment["main"]["feels_like"]
    return round(total_temp / len(forecast_tomorrow), 1)


def calculate_is_rainy(forecast_tomorrow: list) -> bool:
    is_rainy = False
    for increment in forecast_tomorrow:
        for weather in increment["weather"]:
            if weather["main"] == "Rain":
                is_rainy = True
            if weather["main"] == "Drizzle":
                is_rainy = True
            if weather["main"] == "Thunderstorm":
                is_rainy = True
    return is_rainy
