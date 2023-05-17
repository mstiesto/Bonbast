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
    items = ""
    for object in objects.keys():
        items = items + "/" + object + "\n"
    BOT.reply_to(message, items)
@BOT.message_handler(commands=list(objects.keys()))
def list(message):
    BOT.reply_to(message, "salam")
@BOT.message_handler(commands=['currencies', 'coins'])
def send_price(message):
    for currency, ids in currencies.items():
        if message.text == "/" + currency:
            sell = client.get(ids['sellID'])
            buy = client.get(ids['buyID'])
            text = ("Sell: " + str(sell, 'utf-8') + "\n" + "Buy: " + str(buy, 'utf-8'))
            break
    BOT.reply_to(message, text)
BOT.infinity_polling()