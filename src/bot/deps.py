import logging

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand, BotCommandScopeDefault

from src.settings import settings
from src.bot.handlers.basic_handlers import basic_router
from src.bot.handlers.poll_handlers import poll_router


# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=settings.TG_BOT_TOKEN)
dp = Dispatcher(storage=MemoryStorage())
dp.include_router(basic_router)
dp.include_router(poll_router)

# Set bot commands
commands = [
    BotCommand(
        command="start",
        description="Bot description"
    ),
    BotCommand(
        command="help",
        description="Help"
    ),
    BotCommand(
        command="weather",
        description="Weather"
    ),
    BotCommand(
        command="exchange",
        description="Currency exchange calculator"
    ),
    BotCommand(
        command="animals",
        description="Get random animal picture"
    ),
    BotCommand(
        command="poll",
        description="Create a poll"
    ),
    BotCommand(
        command="cancel",
        description="Cancel"
    )
]


async def start_bot():
    try:
        await bot.set_my_commands(commands, BotCommandScopeDefault())
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

