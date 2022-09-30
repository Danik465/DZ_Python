from telegram import Bot
from telegram.ext import Updater, CommandHandler,MessageHandler, Filters, ConversationHandler
from  random import  randint as rd
import wikipedia

bot = Bot(token='5533102869:AAHvRv4Uh_B3t9MmqxUqt9t1nJTr3caDHsc')
updater = Updater(token='5533102869:AAHvRv4Uh_B3t9MmqxUqt9t1nJTr3caDHsc')
dispatcher = updater.dispatcher

A = 0
B = 1
C = 2

def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет\n Как твои дела?')
    return  A

def howareyou(update, context):
    text = update.message.text
    if 'хор' in text.lower():
        context.bot.send_message(update.effective_chat.id, 'Я рад что всё ок')
    else:
        context.bot.send_message(update.effective_chat.id, 'не грусти')
    context.bot.send_message(update.effective_chat.id, 'Как погода?')
    return  B

def weather(update, context):
    text = update.message.text
    context.bot.send_message(update.effective_chat.id, 'Ну ок, у меня тоже сегодня хорошая погода')

    return ConversationHandler.END


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, 'Прощай!')

def rand(update, context):
    context.bot.send_message(update.effective_chat.id, f'{rd(1,100)}')

def voice(update, context):
    text = update.message.text
    if 'прив' in text.lower():
        context.bot.send_message(update.effective_chat.id, 'И тебе привет, мой дорогой друг!')
    else:
        context.bot.send_message(update.effective_chat.id, 'Я тебя не понимаю :(')
def wiki(update, context):
    text = " ".join(context.args)
    try:
        result = wikipedia.summary(text, sentences=2)
        context.bot.send_message(update.effective_chat.id, 'И тебе привет, мой дорогой друг!')
    except:
        context.bot.send_message(update.effective_chat.id, " Не найдено")



start_handler = CommandHandler('start', start)
howareyou_handler = MessageHandler(Filters.text, howareyou)
weather_handler = MessageHandler(Filters.text, weather)
random_handler = CommandHandler('random', rand)
message_handler = MessageHandler(Filters.text, voice)
wiki_handler = CommandHandler('wiki', wiki)
cancel_handler = CommandHandler('cancel', cancel)
conv_handler = ConversationHandler(entry_points=[start_handler],
                                    states={A: [howareyou_handler],
                                            B: [weather_handler]},
                                    fallbacks=[cancel_handler])
dispatcher.add_handler(conv_handler)


dispatcher.add_handler(start_handler)
dispatcher.add_handler(random_handler)
dispatcher.add_handler(wiki_handler)
dispatcher.add_handler(message_handler)


updater.start_polling()
updater.idle()  # ctrl + c


