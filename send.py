import os, telebot
from pymemcache.client import base
client = base.Client(('memcached', 11211))
# currencies = ['eur1', 'eur2', 'usd1', 'usd2']
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
    },
    "lir" : {
        "name" : "lir",
        "buyID" : "try2",
        "sellID" : "try1"
    }
}
BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT = telebot.TeleBot(BOT_TOKEN)
@BOT.message_handler(commands=list(currencies.keys()))
def send_price(message):
    for currency in currencies.values():
        if message.text == "/" + currency['name']:
            sell = client.get(currency['sellID'])
            buy = client.get(currency['buyID'])
            text = ("Sell: " + str(sell, 'utf-8') + "\n" + "Buy: " + str(buy, 'utf-8'))
            break
    BOT.reply_to(message, text)
BOT.infinity_polling()