import cianparser
import pandas as pd
import time
import random

moscow = cianparser.CianParser(location='Москва')
data = []
for i in range(450, 500):
    success = False
    while not success:
        try:
            a = moscow.get_flats(deal_type='sale', rooms=(1,2), additional_settings={'start_page':i, 'end_page': i})
            data.extend(a)
            success = True
        except:
            print('Ошибка')
            print(f'Ошибка на странице {i}')
            time.sleep(10)
            print(f'Спать 10 секунд')
        finally:
            sleep_time = random.uniform(30, 60)
            time.sleep(sleep_time)
            print(f'Спать {sleep_time} секунд')

exel_export = pd.DataFrame(data)
columns = ['author', 'author_type', 'location', 'deal_type', 'accommodation_type', 'floors_count', 'rooms_count', 'total_meters', 'price', 'district', 'street', 'house_number', 'underground', 'residential_complex'] #здесь мы указваем нужны параметры отсортированные через цикл для записи в таблицу
selected_columns = exel_export[columns]
selected_columns.to_csv('cian_parsing.csv', mode='a', header=False, index=False)