import os, telebot, time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT = telebot.TeleBot(BOT_TOKEN)

@BOT.message_handler(commands=['euro', 'dollar'])

def send_price(message):
    url = 'https://bonbast.com/'
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument("window-size=1920x1080")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    # options.add_argument('--disable-dev-shm-usage') # Not used 
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(5)
    src = driver.page_source
    soup = BeautifulSoup(src)
    if message.text == "/euro":
        currency = soup.find(id="eur1")
    elif message.text == "/dollar":
        currency = soup.find(id="usd1")
    else:
        BOT.reply_to(message, "Could not find the currency")
    BOT.reply_to(message, currency)
    driver.close()
BOT.infinity_polling()