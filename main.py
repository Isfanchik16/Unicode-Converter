from telegram.ext import Updater, CommandHandler, ConversationHandler,MessageHandler,Filters
from telegram import BotCommand
import json
from convertor import Unicode_Con,Convert,encode

with open("token.json") as file:
    token = json.load(file)['token']

def start_message(update,context):
    update.message.reply_text(f"Hello {update.effective_user.first_name}! To convert unicode type the command.")
    commands = [BotCommand(command="unicode_to_char",description="Convert unicode to charecter"),
                BotCommand(command="char_to_unicode",description="Convert charecter to unicode"),
                BotCommand(command="encode_text",description="Encode the name or text"),
                BotCommand(command='cancel',description="Cancel. If bot is doing nothing, then type this.")]
    context.bot.set_my_commands(commands=commands)
    print(f"{update.effective_user.id} started")
def unicode_conv1(update,context):
    update.message.reply_text("Send unicode (U+0048): ")
    print(f'user {update.effective_user.id} is sending unicode')
    return "CONVERT_2"
def unicode_conv2(update,context):
    try:
        unicode = update.message.text
        answer = Convert(unicode)
        update.message.reply_text(answer)
        return ConversationHandler.END
    except:
        update.message.reply_text("Error occured, canceled.")
def find_unicode1(update,context):
    update.message.reply_text("Send only one char:")
    return "FIND_UNICODE2"
def find_unicode2(update,context):
    try:
        char = update.message.text
        answer = Unicode_Con(char)
        print(f'user {update.effective_user.id} sent text or name to unicode')
        update.message.reply_text(answer)
        return ConversationHandler.END
    except:
        update.message.reply_text("canceled✖️")
        return ConversationHandler.END
def encode1(update,context):
    update.message.reply_text("Send name or text:")
    return "ENCODE2"
def encode2(update,context):
    try:
        char = update.message.text
        answer = encode(name=char)
        print(f'user {update.effective_user.id} sent char')
        update.message.reply_text(answer)
        return ConversationHandler.END
    except:
        update.message.reply_text("Error occured, canceled.")
def cancel(update,context):
    update.message.reply_text("canceled")
    return ConversationHandler.END

updater = Updater(str(token))
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler(command="start",callback=start_message))
dispatcher.add_handler(ConversationHandler(entry_points=[CommandHandler(command="unicode_to_char",callback=unicode_conv1)],
                                           states={"CONVERT_2":[MessageHandler(Filters.text,unicode_conv2)]},
                                           fallbacks=[CommandHandler(command="cancel",callback=cancel)]))
dispatcher.add_handler(ConversationHandler(entry_points=[CommandHandler("char_to_unicode",find_unicode1)],
                                           states={"FIND_UNICODE2":[MessageHandler(Filters.text,find_unicode2)]},
                                           fallbacks=[CommandHandler('cancel',cancel)]))
dispatcher.add_handler(ConversationHandler([CommandHandler("encode_text",encode1)],
                                           {"ENCODE2":[MessageHandler(Filters.text,encode2)]},
                                           [CommandHandler('cancel',cancel)]))
print('bot is working')
updater.start_polling()
updater.idle()

