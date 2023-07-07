# https://finance.naver.com/item/sise.naver?code=323410

import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/item/sise.naver?code=323410"
response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, "html.parser")
price = soup.select_one("strong.tah.p11")
print(price.text)

