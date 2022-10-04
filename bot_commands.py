from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

from currency_converter import CurrencyConverter 
c = CurrencyConverter()

from pyowm import OWM
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import datetime

from spy import *



def hello(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'Hello {update.effective_user.first_name}')

def exchange(update: Update, context: CallbackContext):      #JPY  GBP  CHF   RUB  EUR  USD
    log(update, context)
    msg = update.message.text
    print(msg)
    items = msg.split()
    x = int(items[1])
    y = str(items[2])
    z = str(items[3])
    update.message.reply_text(f'{x}{y} = {c.convert(x, y, z)}{z}')

def help(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f'/hello\n/time\n/exchange (введите колличество у/е, название валюты 1 и название валюты 2 "JPY  GBP  CHF   RUB  EUR  USD")\n/weather (город)\n/help')

def weath(update: Update, context: CallbackContext):
    log(update, context)
    owm = OWM('159c7438e3201de25aa81e35c2d65c47')
    mgr = owm.weather_manager()
    place = update.message.text
    place = place.split()
    place = place[1]
    print(place)
    observation = mgr.weather_at_place(place)


    w = observation.weather
    # температура
    t = w.temperature('celsius')
    t1 = t['temp']
    t2 = t['feels_like']
    t3 = t['temp_max']
    t4 = t['temp_min']
    # скорость ветра
    ws = w.wind()['speed'] 

    # влажность
    humi = w.humidity

    # облачность
    cl = w.clouds
    update.message.reply_text(
    f'В городе {place} температура {t1}℃ ,\n ощущается как {t2}℃ , максимальная температура {t3}℃ , минимальная темпераьура {t4}℃ ,\nскорость ветра {ws}м/с, влажность {humi}%, облачность {cl}%')  

def time(update: Update, context: CallbackContext):
    log(update, context)
    update.message.reply_text(f' {datetime.datetime.now().time()}')    