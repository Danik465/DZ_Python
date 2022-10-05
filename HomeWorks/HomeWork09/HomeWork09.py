from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from  random import  randint
bot = Bot(token='5533102869:AAHvRv4Uh_B3t9MmqxUqt9t1nJTr3caDHsc')
updater = Updater(token='5533102869:AAHvRv4Uh_B3t9MmqxUqt9t1nJTr3caDHsc')
dispatcher = updater.dispatcher




def start(update, context):
    context.bot.send_message(update.effective_chat.id, f'Привет')

def split(update, context):
    text = update.message.text
    line = list(filter(lambda x: 'абв' not in x, text.split()))
    text = ''
    for i in line:
        text += f"{i} "
    context.bot.send_message(update.effective_chat.id, text)




start_handler = CommandHandler('start', start)
split_handler = MessageHandler(Filters.text, split)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(split_handler)


updater.start_polling()
updater.idle()  # ctrl + c