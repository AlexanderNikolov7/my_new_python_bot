from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from bot_commands import *

# from currency_converter import CurrencyConverter 
# c = CurrencyConverter()

def hello(update: Update, context: CallbackContext):
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

updater = Updater('5132667274:AAFpfSnPJIeycfkt2OQxHoNEfYSfEC_DBR0')

updater.dispatcher.add_handler(CommandHandler('hello' , hello))

updater.dispatcher.add_handler(CommandHandler('exchange' , exchange))

updater.dispatcher.add_handler(CommandHandler('time', time))

updater.dispatcher.add_handler(CommandHandler('help', help))

updater.dispatcher.add_handler(CommandHandler('weather', weath))


print('server start')

updater.start_polling()
updater.idle()