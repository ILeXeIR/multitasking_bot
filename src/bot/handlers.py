import datetime
import json

from aiogram import F, Router, types
from aiogram.filters import Command
import aiohttp

from src.settings import settings as s

handlers_router = Router()


@handlers_router.message(Command(commands=["start"]))
async def send_welcome(message: types.Message):
    await message.answer("Hi! I'm MultitaskingBot!\n"
                         "Choose one of commands from Menu.\n"
                         "For more information use /help")


@handlers_router.message(Command(commands=["help"]))
async def send_instruction(message: types.Message):
    await message.answer("instruction")


@handlers_router.message(Command(commands=["weather"]))
async def send_weather(message: types.Message):
    weather_url = f"https://api.openweathermap.org/data/2.5/weather?q=London&appid={s.WEATHER_API_KEY}"
    async with aiohttp.ClientSession() as session:
        async with session.get(weather_url) as resp:
            print(resp.status)
            await message.answer(await resp.text())
