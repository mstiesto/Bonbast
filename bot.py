import os, telebot, requests, dryscrape
from bs4 import BeautifulSoup

BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT = telebot.TeleBot(BOT_TOKEN)

@BOT.message_handler(commands=['start', 'hello'])
def send_price(message):
    url     = 'https://bonbast.com/'
    session = dryscrape.Session()
    session.visit(url)
    response = session.body()
    soup = BeautifulSoup(response)
    euro = soup.find(id="euro1")
    BOT.reply_to(message, euro)
BOT.infinity_polling()