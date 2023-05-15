import os, telebot, yaml
from pymemcache.client import base
client = base.Client(('memcached', 11211))
with open("objects.yaml") as o:
    objects = yaml.load(o, Loader=yaml.FullLoader)
    currencies = objects['currencies']
    coins = objects['coins']
BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT = telebot.TeleBot(BOT_TOKEN)
@BOT.message_handler(commands=['start'])
def start(message):
    BOT.reply_to(message, list(objects))

@BOT.message_handler(commands=list(objects))
def list(message):
    for object, values in objects.items():
        if message.text == "/" + object:
            BOT.reply_to(message, list(values))

@BOT.message_handler(commands=list(currencies.keys()))
def send_price(message):
    for currency, ids in currencies.items():
        if message.text == "/" + currency:
            sell = client.get(ids['sellID'])
            buy = client.get(ids['buyID'])
            text = ("Sell: " + str(sell, 'utf-8') + "\n" + "Buy: " + str(buy, 'utf-8'))
            break
    BOT.reply_to(message, text)
BOT.infinity_polling()