import time
from bs4 import BeautifulSoup
from selenium import webdriver
from pymemcache.client import base
client = base.Client(('memcached', 11211))
currencies = ['eur1', 'eur2', 'usd1', 'usd2']
while True:
    print("Geting price list ...")
    url = 'https://bonbast.com'
    options = webdriver.ChromeOptions()
    options.add_argument('--headless=new')
    options.add_argument('--disable-dev-shm-usage')
    # options.add_argument("window-size=1024x768")
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    options.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0")
    driver = webdriver.Chrome(options=options)
    driver.set_page_load_timeout(30)
    driver.get(url)
    time.sleep(5)
    src = driver.page_source
    soup = BeautifulSoup(src, 'html.parser')
    for currency in currencies:
        price = soup.find(id=currency)
        print("price for", currency, "is: ", price.get_text())
        client.set(currency, price.get_text())
    driver.quit()
    time.sleep(300)