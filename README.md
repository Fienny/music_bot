# Telegram bot for sending mp3 file from YouTube link

---

#### Hi there! This is the source code of telegram bot - music sender

---

### How it works?

Very simple. User starts the bot and afterward he has two options: to get audio or get help. Well, regarding the button 
they press, they could get mp3 file extracted from the link on YouTube video sent or get some help
on usage.

---
### What was used to create?
1. pyTelegramBotAPI 
2. library named "pytube" to work with YouTube videos
3. python-dotenv to store TOKEN for safety 
---
### How to install it?
* Get token from [BotFather](https://t.me/BotFather)
* Download whole repository and unzip it to a folder
* Create virtual environment
* Install everything from _requirements.txt_ (pip install "name")
* Setup .env file ([Guide](https://pypi.org/project/python-dotenv/))
* Add ```TOKEN="your token"``` to your .env file

Now you are ready to start your bot! Run bot.py and enjoy :)
