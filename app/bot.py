from telebot.async_telebot import AsyncTeleBot

from app.config import settings

bot = AsyncTeleBot(settings.TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=["help", "start"])
async def send_welcome(message):
    await bot.reply_to(message, "Repply")


@bot.message_handler(func=lambda message: True)
async def echo_message(message):
    await bot.reply_to(message, message.text)
