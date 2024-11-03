from telegram.ext import Updater, CommandHandler, ConversationHandler,MessageHandler,Filters
from telegram import BotCommand
import json
from convertor import Unicode_Con,Convert

with open("token.json") as file:
    token = json.load(file)

def start_message(update,context):
    update.message.reply_text(f"Hello {update.effective_user.name}! To convert unicode type the command.")
    commands = [BotCommand(command="unicode_to_char",description="Convert unicode to charecter"),
                BotCommand(command="char_to_unicode",description="Convert charecter to unicode")]
    context.bot.set_my_commands(commands=commands)
def unicode_conv1(update,context):
    update.message.reply_text("Send unicode: ")
    return "CONVERT_2"
def unicode_conv2(update,context):
    unicode = update.message.text
    answer = Convert(unicode)
    update.message.reply_text(answer)
    return ConversationHandler.END
def find_unicode1(update,context):
    update.message.reply_text("Send only one char:")
    return "FIND_UNICODE2"
def find_unicode2(update,context):
    char = update.message.text
    answer = Unicode_Con(char)
    update.message.reply_text(answer)
    return ConversationHandler.END
def cancel(update,context):
    return ConversationHandler.END

updater = Updater(token)
dispatcher = updater.dispatcher()
dispatcher.add_handler(CommandHandler(command="start",callback=start_message))
dispatcher.add_handler(ConversationHandler(entry_points=[CommandHandler(command="unicode_to_char",callback=unicode_conv1)],
                                           states={"CONVERT_2":[MessageHandler(Filters.text,unicode_conv2)]},
                                           fallbacks=[CommandHandler(command="cancel",callback=cancel)]))
updater.start_polling()
updater.idle()

