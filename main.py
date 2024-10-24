from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.cian.ru/kupit-kvartiru-1-komn-ili-2-komn/'

parsing = requests.get(url)
soup = BeautifulSoup(parsing.text, 'html.parser')
cards = soup.find_all('div', 'data_name=')
# pretty_html = soup.prettify()

print(cards)

# print(pretty_html)

# for i in cards:
#     print(i)