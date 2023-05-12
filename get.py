import time
from datetime import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from pymemcache.client import base
client = base.Client(('memcached', 11211))

#currencies = ["euro", "dollar"]

currencies = {
    "euro" : {
        "name" : "euro",
        "buyID" : "eur2",
        "sellID" : "eur1"
    },
    "dollar" : {
        "name" : "dollar",
        "buyID" : "usd2",
        "sellID" : "usd1"
    }
}
def fetchData():
    print(datetime.now(), "Geting price list ...")
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
    driver.quit()
    return soup
def iteratePrice(soup, name, sellID, buyID):
    print(datetime.now(), "Getting data for", name)
    sellPrice = soup.find(id=sellID)
    buyPrice = soup.find(id=buyID)
    return buyPrice, sellPrice
def setPrice(name, id, price):
    print(datetime.now(), "Setting", price.get_text(), "for", name, id, "...")
    client.set(id, price.get_text())

while True:
    soup = fetchData()
    for currency in currencies.values():
        name = currency["name"]
        sellID = currency["sellID"]
        buyID = currency["buyID"]
        buyPrice, sellPrice = iteratePrice(soup, name, sellID, buyID)
        setPrice(name ,buyID, buyPrice)
        setPrice(name, sellID, sellPrice)
    time.sleep(1800)