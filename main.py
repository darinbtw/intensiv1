from bs4 import BeautifulSoup
import requests
import os
import time

if not os.path.exists('images'):
    os.mkdir('images')

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'}
base_url = "https://shikimori.one/animes/page/{}"
image_counter = 0

for page_number in range(1,10):
    url = base_url.format(page_number)
    page = requests.get(url, headers=header)
    soup = BeautifulSoup(page.text, 'html.parser')
    
    images = soup.find_all('img')
    for image in images:
        image_url = image['src']
        image_data = requests.get(image_url).content
        with open('images/img{}.jpg'.format(image_counter), 'wb') as handler:
            handler.write(image_data)
        image_counter += 1
        time.sleep(2)
        print('Image {} скачивается'.format(image_counter))

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



