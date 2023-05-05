import os, telebot
from playwright.sync_api import Playwright, sync_playwright
from bs4 import BeautifulSoup

BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT = telebot.TeleBot(BOT_TOKEN)


@BOT.message_handler(commands=['euro', 'dollar'])
def send_price(message):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Load the web page
        page.goto('https://bonbast.com')

        # Perform actions to load dynamic content here
        # ...

        # Get the HTML content of the page
        html = page.content()

        # Extract the data you want using a Python HTML parsing library like BeautifulSoup or lxml
        soup = BeautifulSoup(html, 'html.parser')

        # Extract data from the soup object here
        if message.text == "/euro":
            currency = soup.find(id="eur1")
        elif message.text == "/dollar":
            currency = soup.find(id="usd1")
        else:
            BOT.reply_to(message, "Could not find the currency")
        BOT.reply_to(message, currency.prettify())
        # Close the browser
        browser.close()

    BOT.infinity_polling()