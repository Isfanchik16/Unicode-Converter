from telegram.ext import Updater, CommandHandler
from telegram import KeyboardButton
import json

with open("token.json") as file:
    token = json.load(file)

def start_message(update,context):
    update.message.reply_text(f"Hello {update.effective_user.name}! To convert unicode type command /convert")

updater = Updater(token)
dispatcher = updater.dispatcher()
dispatcher.add_handler(CommandHandler(command="start",callback=start_message))
updater.start_polling()
updater.idle()

