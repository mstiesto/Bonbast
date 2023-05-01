import os, telebot, requests
from bs4 import BeautifulSoup

BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT = telebot.TeleBot(BOT_TOKEN)

@BOT.message_handler(commands=['start', 'hello'])
def send_price(message):
    url = 'https://bonbast.com'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    euro = soup.find(id="eur1")
    BOT.reply_to(message, euro)
BOT.infinity_polling()