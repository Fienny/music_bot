import os
import telebot
from dotenv import load_dotenv
from logics.bots_chat import keyboard, send_help, get_link
from logics.get_music import get_music, delete_file

# Import env vars
load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hello there 😀. This bot sends you mp3 from the youtube link 🙂.",
                     reply_markup=keyboard())


@bot.message_handler(content_types=['text'])
def answer(message):
    if message.text == "Help":
        send_help(message)
    if message.text == "Get audio":
        msg = bot.send_message(message.chat.id, "Send me the link now:")
        bot.register_next_step_handler(msg, get_link)


bot.infinity_polling()
