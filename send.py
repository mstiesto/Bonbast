import os, telebot
from pymemcache.client import base

client = base.Client(('memcached', 11211))
currencies = ['eur1', 'eur2', 'usd1', 'usd2']

BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT = telebot.TeleBot(BOT_TOKEN)
@BOT.message_handler(commands=['euro', 'dollar'])
def send_price(message):
    if message.text == "/euro":
        currency = client.get('eur1')
    elif message.text == "/dollar":
        currency = client.get('usd1')
    else:
        BOT.reply_to(message, "Could not find the currency")    
    BOT.reply_to(message, currency)


BOT.infinity_polling()