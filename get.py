import time
from bs4 import BeautifulSoup
from selenium import webdriver
from pymemcache.client import base
client = base.Client(('memcached', 11211))

#currencies = ["euro", "dollar"]

Currencies = {
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

class Currency:
    name=""
    buyID=""
    sellID=""
    def setPrice(slef, id, price):
        client.set(id, price.get_text())

def fetchData():
    print("Geting price list ...")
    url = 'https://bonbast.com'
    options = webdriver.ChromeOptions()
    options.add_argument('--headldollaress=new')
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

def iteratePrice(Currency):
    print("Getting data for", Currency)
    soup = fetchData()
    sellPrice = soup.find(id=Currency.sellID)
    buyPrice = soup.find(id=Currency.buyID)
    return buyPrice, sellPrice


while True:
    for Currency in Currencies:
        print("Set price for", Currency,"...")
        buyPrice, sellPrice = iteratePrice(Currency)
        Currency.setPrice(Currency.buyID, buyPrice)
        Currency.setPrice(Currency.sellID, sellPrice)
    time.sleep(300)