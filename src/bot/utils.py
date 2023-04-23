import json
from typing import Union


def get_weather_text(weather_resp: str) -> str:
    # Return text with main weather params from JSON string or error message
    weather_dict = json.loads(weather_resp)
    if weather_dict.get("message") is not None:
        return weather_dict["message"].capitalize()  # Error message
    pressure = int(weather_dict["main"]["pressure"]) * 0.75  # From hPa to mmHg
    description = weather_dict['weather'][0]['description'].capitalize()
    weather_text = f"Current weather in {weather_dict['name']}, " \
                   f"{weather_dict['sys']['country']}:\n" \
                   f"Temperature: {weather_dict['main']['temp']}°C\n" \
                   f"{description}\n" \
                   f"Pressure: {pressure} mmHg\n" \
                   f"Humidity: {weather_dict['main']['humidity']}%\n" \
                   f"Wind: {weather_dict['wind']['speed']} m/s"
    return weather_text


def get_animal_photo(animal_resp: str) -> str:
    # Return image's URL from JSON string
    animal_dict = json.loads(animal_resp)
    return animal_dict["urls"]["regular"]


def get_exchange_params(query: str) -> Union[str, tuple[str, str, str]]:
    # Parse message text and return ('amount', 'currency_from', 'currency_to') or string 'error'
    query_list = query.split()
    if len(query_list) != 4 or query_list[2] != "to":
        return "error"
    else:
        return query_list[0], query_list[1], query_list[3]


def get_exchange_result(exchange_resp: str) -> str:
    # Return exchange result or string 'error' from JSON string
    exchange_dict = json.loads(exchange_resp)
    if exchange_dict.get("error") is not None:
        return "error"
    return exchange_dict["result"]
