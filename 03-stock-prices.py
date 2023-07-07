# https://finance.naver.com/item/sise.naver?code=323410, 005380, 105560

import requests
from bs4 import BeautifulSoup

codes = ["323410","005380","105560"]
url = "https://finance.naver.com/item/sise.naver?code=%s"
prices = []

for code in codes : 

    response = requests.get(url % code)
    html = response.text

    soup = BeautifulSoup(html, "html.parser")
    price = soup.select_one("strong.tah.p11")
    prices.append(price.text)

print(prices)

