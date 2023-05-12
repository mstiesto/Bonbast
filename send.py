import os, telebot
from pymemcache.client import base

client = base.Client(('memcached', 11211))
currencies = ['eur1', 'eur2', 'usd1', 'usd2']

currencies = {
    "euro" : {
        "name" : "euro",
        "buyID" : "eur2",
        "sellID" : "eur1"
    },
    "dollar" : {
        "name" : "dollar",
        "buyID" : "usd2",
        "sellID" : "usd1"
    }
}

BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT = telebot.TeleBot(BOT_TOKEN)
@BOT.message_handler(commands=list(currencies.keys()))
def send_price(message):
    if message.text == "/euro":
        sell = client.get('eur1')
        buy = client.get('eur2')
    elif message.text == "/dollar":
        sell = client.get('usd1')
        buy = client.get('usd2')
    else:
        BOT.reply_to(message, "Could not find the currency")
    text = print("Sell:", sell, "\nBuy:", buy)
    BOT.reply_to(message, text)


BOT.infinity_polling()