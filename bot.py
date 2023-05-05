import os, telebot, dryscrape, webkit_server

from bs4 import BeautifulSoup


BOT_TOKEN = os.environ.get('BOT_TOKEN')
BOT = telebot.TeleBot(BOT_TOKEN)


@BOT.message_handler(commands=['euro', 'dollar'])


sess = dryscrape.Session(driver=driver)



def send_price(message):
    url = 'https://bonbast.com/'
    server = webkit_server.Server()
    server_conn = webkit_server.ServerConnection(server=server)
    driver = dryscrape.driver.webkit.Driver(connection=server_conn)

#    dryscrape.start_xvfb()
    session = dryscrape.Session(driver=driver)
    session.set_header('user-agent', 'Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36')
    session.set_attribute('auto_load_images', False)
    session.set_timeout(30)
    session.visit(url)
    response = session.body()
    session.reset()
    server.kill()
    soup = BeautifulSoup(response, features="lxml")
    if message.text == "/euro":
        currency = soup.find(id="eur1")
    elif message.text == "/dollar":
        currency = soup.find(id="usd1")
    else:
        BOT.reply_to(message, "Could not find the currency")
    BOT.reply_to(message, currency)
BOT.infinity_polling()
