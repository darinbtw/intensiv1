import cianparser
import pandas as pd
import time

moscow = cianparser.CianParser(location='Москва')
# data = moscow.get_flats(deal_type='sale', rooms=(1,2), additional_settings={'start_page': 4, 'end_page':100} )
# sorted_price = sorted(data, key=lambda x: x['price'])
# print(sorted_price)

data = []
for i in range(1, 20):
    a = moscow.get_flats(deal_type='sale', rooms=(1,2), with_extra_data=True, additional_settings={'start_page': i, 'end_page':i} )
    data.extend(a)
    time.sleep(10)

exel_export = pd.DataFrame(data)
columns = ['author', 'author_type', 'url', 'location', 'deal_type', 'accommodation_type', 'floor', 'floors_count', 
                   'rooms_count', 'total_meters', 'price_per_month', 'commissions', 'price', 'year_of_construction', 
                   'object_type', 'house_material_type', 'heating_type', 'finish_type', 'living_meters', 'kitchen_meters', 
                   'phone', 'district', 'street', 'house_number', 'underground', 'residential_complex']
selected_columns = exel_export[columns]
selected_columns.to_csv('cian_parsing.csv', mode='a', header=False, index=False)
