import os, telebot, yaml
from pymemcache.client import base
client = base.Client(('memcached', 11211))
with open("currencies.yaml") as c:
    currencies = yaml.load(c, Loader=yaml.FullLoader)['currencies']
BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT = telebot.TeleBot(BOT_TOKEN)
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