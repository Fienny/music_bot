import os
import telebot
from dotenv import load_dotenv
from telebot import types

from logics.get_music import get_music, delete_file

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))


def keyboard():
    markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=False)
    send_link = types.KeyboardButton(text="Get audio")
    send_help = types.KeyboardButton(text="Help")
    markup_reply.add(send_link, send_help)
    return markup_reply


def send_help(message):
    bot.send_message(message.chat.id, "Hello there 😀. This bot sends you mp3 from the youtube link.")


def get_link(message):
    path = get_music(message.text)
    audio = open(path, 'rb')
    bot.send_audio(message.chat.id, audio)
    audio.close()
    delete_file(path)

