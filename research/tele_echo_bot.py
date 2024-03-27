import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN = os.getenv("TOKEN")

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def command_start_handler(message: types.Message):
    """
    This handler receives messages with `/start` or `/help` command
    """
    await message.reply("Hi\nI am Echo Bot!\nPowered by aiogram.")


@dp.message_handler()
async def echo(message: types.Message):
    """
    This will return echo
    """
    await message.answer(message.text)


async def start_bot():
    # Start polling
    await dp.start_polling()


if __name__ == "__main__":
    # Create and run event loop
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
