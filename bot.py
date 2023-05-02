import os, telebot, requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT = telebot.TeleBot(BOT_TOKEN)


@BOT.message_handler(commands=['start', 'hello'])
def send_price(message):
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(options=chrome_options)
    url     = 'https://bonbast.com/'
    driver  = webdriver.PhantomJS()
    driver.get(url)
    euro = driver.find_element_by_id(id_='euro1')
    BOT.reply_to(message, euro)
BOT.infinity_polling()