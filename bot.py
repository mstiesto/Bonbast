import os, telebot, requests
from bs4 import BeautifulSoup


url = 'https://bonbast.com'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')

BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT = telebot.TeleBot(BOT_TOKEN)

@BOT.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    BOT.reply_to(message, soup)
BOT.infinity_polling()