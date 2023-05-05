import os, telebot
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT = telebot.TeleBot(BOT_TOKEN)


@BOT.message_handler(commands=['euro', 'dollar'])

def send_price(message):
    url = 'https://bonbast.com/'
    options = Options()
    options.add_argument("--headless")
    browser= webdriver.Firefox(firefox_options=options, executable_path="/usr")
    browser.get(url);
    soup = BeautifulSoup(response, features="lxml")
    if message.text == "/euro":
        currency = soup.find(id="eur1")
    elif message.text == "/dollar":
        currency = soup.find(id="usd1")
    else:
        BOT.reply_to(message, "Could not find the currency")
    BOT.reply_to(message, currency)
    browser.quit()
BOT.infinity_polling()
