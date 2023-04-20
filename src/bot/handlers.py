from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import aiohttp

from src.settings import settings as s
from .utils import get_weather_text, get_animal_photo


handlers_router = Router()


class BotStates(StatesGroup):
    weather_state = State()


@handlers_router.message(Command(commands=["start"]))
async def send_welcome(message: types.Message):
    await message.answer("Hi! I'm MultitaskingBot!\n"
                         "Choose one of commands from Menu.\n"
                         "For more information use /help")


@handlers_router.message(Command(commands=["help"]))
async def send_instruction(message: types.Message):
    await message.answer("instruction")


@handlers_router.message(Command(commands="cancel"))
async def cancel_state(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return None
    await state.clear()
    await message.answer("You canceled this command.")


@handlers_router.message(Command(commands=["weather"]))
async def ask_city(message: types.Message, state: FSMContext):
    await state.set_state(BotStates.weather_state)
    await message.answer("Write a city and I show you current weather there.\n"
                         "Or use /cancel to quit this command")


@handlers_router.message(BotStates.weather_state)
async def send_weather(message: types.Message, state: FSMContext):
    city = message.text.strip().lower()
    weather_url = "https://api.openweathermap.org/data/2.5/weather?" \
                  f"q={city}&units=metric&appid={s.WEATHER_API_KEY}"
    async with aiohttp.ClientSession() as session:
        async with session.get(weather_url) as resp:
            weather_text = get_weather_text(await resp.text())
            await state.clear()
            await message.answer(weather_text)


@handlers_router.message(Command(commands=["animals"]))
async def send_random_animal(message: types.Message):
    animal_url = "https://api.unsplash.com/photos/random/?" \
                 f"client_id={s.UNSPLASH_ACCESS_KEY}&query=cute%20animal"
    async with aiohttp.ClientSession() as session:
        async with session.get(animal_url) as resp:
            photo_link = get_animal_photo(await resp.text())
            await message.answer(photo_link)

