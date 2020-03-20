from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler
import random
import os
import requests

def doit_callback(bot, update):
    bot.send_message(
        chat_id=update.message.chat_id,
        text="SÓ FAÇA!"
    )
    bot.send_message(
        chat_id=update.message.chat_id,
        text="Não deixe que seus sonhos permaneçam sonhos!"
    )
    bot.send_message(
        chat_id=update.message.chat_id,
        text="*JUST*",
	parse_mode = 'Markdown'
    )
    bot.send_message(
        chat_id=update.message.chat_id,
        text="*DO*",
	parse_mode = 'Markdown'
    )
    bot.send_message(
        chat_id=update.message.chat_id,
        text="*IT!*",
	parse_mode = 'Markdown'
    )
    bot.send_message(
        chat_id=update.message.chat_id,
        text="*DO IT!*",
	parse_mode = 'Markdown'
    )
    bot.sendDocument(
        chat_id = update.message.chat_id,
        document = doc
        )


def clap_callback(bot, update):
    bot.sendDocument(
        chat_id=update.message.chat_id,
        document = os.environ["PALMAS_URL"]
    )


def webhook(request):
    bot = Bot(token=os.environ["TELEGRAM_TOKEN"])
    random.seed(a=None, version=2)
    aleatorio =  random.randrange(1 ,1001, 1)

    dispatcher = Dispatcher(bot, None, 0)
    global doc
    if aleatorio%2 == 0:
        doc = os.environ["DOIT_URL"]
    else:
        doc = os.environ["DOIT_ALT_URL"]

    dispatcher.add_handler(
        CommandHandler('doit', doit_callback)
    )
    dispatcher.add_handler(
        CommandHandler('palmas', clap_callback)
    )

    if request.method == 'POST':
        update = Update.de_json(request.get_json(force=True), bot)
        dispatcher.process_update(update)
    return 'ok'

