# 19BCE0619
# Mihir Gupta
from bs4 import BeautifulSoup
import requests
URL = 'https://www.amazon.in/Logitech-Wireless-Lightweight-Programmable-POWERPLAY-Compatible/dp/B07M5DK18R/ref=sr_1_4?keywords=logitech+wireless+gaming+mouse&qid=1645936637&smid=A14CZOWI0VEHLG&sprefix=logitech+wireless+g%2Caps%2C240&sr=8-4'
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36", "Accept-Encoding": "gzip, deflate",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
page = requests.get(URL, headers=headers)
soup1 = BeautifulSoup(page.content, "html.parser")
soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
title = soup2.find(id='productTitle').get_text().strip()
discount = soup2.select_one('.a-color-price').get_text().strip()
price = soup2.select_one('.a-offscreen').get_text().strip()
img = soup2.find(id='landingImage')['src'].strip()
print("Title: ", title)
print("Price: ", price)
print("Discount: ", discount)
print("Image: ", img)
