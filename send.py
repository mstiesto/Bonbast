import os, telebot, yaml
from datetime import datetime
from pymemcache.client import base
client = base.Client(('memcached', 11211))
with open("objects.yaml") as o:
    objects = yaml.load(o, Loader=yaml.FullLoader)
    objectsList = list(objects.keys())
    itemList = []
for item in objects.values():
    itemList = itemList + list(item.keys())
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
            print(datetime.now() , "---" message.from_user.first_name, "---", message.text)
            for object in v.keys():
                item = item + "/" + object + "\n"
    print(item)
    BOT.reply_to(message, item)


@BOT.message_handler(commands=itemList)
def send_price(message):
    for object in objects.values():
        for k, v in object.items():
            if message.text == "/" + k:
                sell = client.get(v['sellID'])
                buy = client.get(v['buyID'])
                text = ("Sell: " + str(sell, 'utf-8') + "\n" + "Buy: " + str(buy, 'utf-8'))
                break
    BOT.reply_to(message, text)
BOT.infinity_polling()