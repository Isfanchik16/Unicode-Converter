from telegram.ext import Updater
# from telegram import KeyboardButton
import json

with open("token.json") as file:
    token = json.load(file)

def start_message(update,context):
    update.message.reply_text(f"Hello {update.effective_user.name}! To calculate unicode type command /calculate")

updater = Updater(token)