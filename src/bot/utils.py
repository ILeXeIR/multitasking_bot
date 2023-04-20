import json


def get_weather_text(weather_resp: str) -> str:
    weather_dict = json.loads(weather_resp)
    if weather_dict.get("message") is not None:
        return weather_dict["message"].capitalize()
    pressure = int(weather_dict["main"]["pressure"]) * 0.75
    description = weather_dict['weather'][0]['description'].capitalize()
    weather_text = f"Current weather in {weather_dict['name']}, " \
                   f"{weather_dict['sys']['country']}:\n" \
                   f"Temperature: {weather_dict['main']['temp']}°C\n" \
                   f"{description}\n" \
                   f"Pressure: {pressure} mmHg\n" \
                   f"Humidity: {weather_dict['main']['humidity']}%\n" \
                   f"Wind: {weather_dict['wind']['speed']} m/s"
    return weather_text


def get_animal_photo(animal_resp: str):
    animal_dict = json.loads(animal_resp)
    return animal_dict["urls"]["regular"]
