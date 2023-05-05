import os, telebot, dryscrape
from bs4 import BeautifulSoup

BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT = telebot.TeleBot(BOT_TOKEN)


@BOT.message_handler(commands=['euro', 'dollar'])
def send_price(message):
    url = 'https://bonbast.com/'
    dryscrape.start_xvfb()
    session = dryscrape.Session()
    session.visit(url)
    response = session.body()
    soup = BeautifulSoup(response, features="lxml")
    if message.text == "/euro":
        currency = soup.find(id="eur1")
    elif message.text == "/dollar":
        currency = soup.find(id="usd1")
    else:
        BOT.reply_to(message, "Could not find the currency")
    BOT.reply_to(message, currency.prettify())
BOT.infinity_polling()
