from config import bot_token
from aiogram import Bot, Dispatcher


bot = Bot(token=bot_token)
dp = Dispatcher(bot)
