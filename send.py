import os, telebot, yaml
from pymemcache.client import base
client = base.Client(('memcached', 11211))
with open("objects.yaml") as o:
    objects = yaml.load(o, Loader=yaml.FullLoader)
    objectsList = list(objects.keys())
    currencies = objects['currencies']
    currenciesList = list(currencies.keys())
    coins = objects['coins']
BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT = telebot.TeleBot(BOT_TOKEN)

@BOT.message_handler(commands=['start'])
def start(message):
    items = ""
    for object in objects.keys():
        items = items + "/" + object + "\n"
    BOT.reply_to(message, items)

@BOT.message_handler(commands=objectsList)
def list(message):
    item = ""
    for k, v in objects.items():
        if message.text == "/" + k:
            print(k)
            for object in v.keys():
                item = item + "/" + object + "\n"
                break
    print(item)
    BOT.reply_to(message, item)

@BOT.message_handler(commands=currenciesList)
def send_price(message):
    for currency, ids in objects['currencies'].items():
        if message.text == "/" + currency:
            sell = client.get(ids['sellID'])
            buy = client.get(ids['buyID'])
            text = ("Sell: " + str(sell, 'utf-8') + "\n" + "Buy: " + str(buy, 'utf-8'))
            break
    BOT.reply_to(message, text)
BOT.infinity_polling()