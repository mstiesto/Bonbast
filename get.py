import time
from bs4 import BeautifulSoup
from selenium import webdriver
from pymemcache.client import base

client = base.Client(('memcached', 11211))
currencies = ['eur1', 'eur2', 'usd1', 'usd2']

url = 'https://bonbast.com/'
options = webdriver.ChromeOptions()
options.add_argument('--headless=new')
options.add_argument("window-size=1920x1080")
options.add_argument('--no-sandbox')
options.add_argument('--disable-gpu')
driver = webdriver.Chrome(options=options)

while True:
    print("Geting price list ...")
    driver.get(url)
    time.sleep(5)
    src = driver.page_source
    soup = BeautifulSoup(src, 'html.parser')
    for currency in currencies:
        price = soup.find(id=currency)
        print(time, "price for", currency, "is: ", price.get_text())
        client.set(currency, price.get_text())
    driver.close()
    time.sleep(1800)