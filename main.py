import cianparser
import pandas as pd
import time

moscow = cianparser.CianParser(location='Москва')
# data = moscow.get_flats(deal_type='sale', rooms=(1,2), additional_settings={'start_page': 4, 'end_page':100} )
# sorted_price = sorted(data, key=lambda x: x['price'])
# print(sorted_price)

data = []
for i in range(83, 100):
    a = moscow.get_flats(deal_type='sale', rooms=(1,2), additional_settings={'start_page': i, 'end_page':i} )
    data.extend(a)
    time.sleep(10)

exel_export = pd.DataFrame(data)
columns = ['author', 'author_type', 'location', 'deal_type', 'accommodation_type', 'floors_count', 'rooms_count', 'total_meters', 'price', 'district', 'street', 'house_number', 'underground', 'residential_complex']
selected_columns = exel_export[columns]
selected_columns.to_csv('cian_parsing.csv', mode='a', header=False, index=False)

