import os, telebot, time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pymemcache.client import base

client = base.Client(('memcached', 11211))

BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT = telebot.TeleBot(BOT_TOKEN)
@BOT.message_handler(commands=['euro', 'dollar'])

def send_price(message):
    if message.text == "/euro":
        currency = client.get('eur1')
    elif message.text == "/dollar":
        currency = client.get('usd1')
    else:
        BOT.reply_to(message, "Could not find the currency")    
    BOT.reply_to(message, currency)


BOT.infinity_polling()

def get_price():
    currencies = ['eur1', 'eur2', 'usd1', 'usd2']
    url = 'https://bonbast.com/'
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument("window-size=1920x1080")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)
    driver.close()
    src = driver.page_source
    soup = BeautifulSoup(src)
    for currency in currencies:
        price = soup.find(id=currency)
        client.set(currency, price)

while True:
    get_price()
    time.sleep(1800)