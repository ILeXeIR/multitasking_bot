# Multitasking Telegram Bot
___
## About the project:
This project is a Telegram bot that can check the weather in any city, convert currencies, make you smile by showing a charming animals, and assist you in creating polls.

The bot is built using **Python** with asynchronous frameworks:
- **aiogram 3**
- **aiohttp**
- **pydantic**

___
## Available commands:

- _/start_ - just greeting
- _/cancel_ - exit from dialog with any command in any moment
- _/weather_ - write a name of a city. Bot shows current weather there.
Example of query: 'London'.
- _/exchange_ - write currency exchange query. Bot shows conversion result.
Use three-letter currency codes.
Example of query: '5.35 EUR to GBP'.
- _/animals_ - bot sends you a random cute animal photo
- _/poll_ - poll constructor.
Bot asks you to write poll question, answer options and poll parameters. 
After that, it creates a new poll.

___
## Installation
**1.** Clone this repository.

**2.** Create Telegram bot via @BotFather. 
Copy and save the Telegram bot's access token.

**3.** Create an account on https://openweathermap.org/ and save API key.

**4.** Create an account on https://exchangeratesapi.io/ and save API key.

**5.** Create an account on https://unsplash.com/, create an app and save Access Key.

**6.** Open the project folder and create .env file with the following environmental variables:
```commandline
TG_BOT_TOKEN="<your_token_from_point_2>"
WEATHER_API_KEY="<your_key_from_point_3>"
EXCHANGERATE_API_KEY="<your_key_from_point_4>"
UNSPLASH_ACCESS_KEY="<your_key_from_point_5>"
```

**7.** Install Python if required (https://www.python.org/downloads/).

**8.** Create a virtual environment in the project folder: ```python -m venv env``` 
  (or use command “python3” here and below, if “python” doesn’t work).

**9.** Activate the virtual environment: 

  ```env\Scripts\activate``` (for Windows) 

  ```source env/bin/activate``` (for Linux/Mac) 

**10.** Run ```pip install -r requirements.txt```.

**11.** Start app with ```python main.py```

