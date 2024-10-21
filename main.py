from bs4 import BeautifulSoup
import requests
import os
import time

if not os.path.exists('images'):
    os.mkdir('images')

# page = requests.get(url, headers=headers)
# soup = BeautifulSoup(page.text, 'html.parser')
# print(soup.prettify())
# print(page.status_code)

# links = soup.find_all('img')
# for link in links:
#     print(link['src'])

# for i, url in enumerate(soup.find_all('img')):
#     time.sleep(2)
#     img_url = url['src']
#     img_data = requests.get(img_url).content
#     with open('images/img{}.jpg'.format(i), 'wb') as handler:
#         handler.write(img_data)

def get_image(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.text, 'html.parser')
    links = soup.find_all('img')
    for i, url in enumerate(links):
        time.sleep(2)
        img_url = url['src']
        img_data = requests.get(img_url).content
        with open('images/img{}.jpg'.format(i), 'wb') as handler:
            handler.write(img_data)

url = 'https://shikimori.one/animes'


