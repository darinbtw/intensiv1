import cianparser
import pandas as pd
import time

moscow = cianparser.CianParser(location='Долгопрудный')

data = []
request_count = 0  # Счётчик запросов

for i in range(1, 50):
    # Получаем данные за текущую страницу
    a = moscow.get_flats(deal_type='sale', rooms=(1,2), with_extra_data=True, additional_settings={'start_page': i, 'end_page':i} )
    data.extend(a)
    
    # Увеличиваем счётчик запросов
    request_count += 1
    
    # Пауза на 1 минуту после каждых 10 запросов
    if request_count % 10 == 0:
        print(f"Пауза на 1 минуту после {request_count} запросов...")
        time.sleep(60)
    
    # Пауза на 10 секунд между всеми запросами
    time.sleep(10)

# Экспорт данных в CSV
exel_export = pd.DataFrame(data)
columns = ['author', 'author_type', 'url', 'location', 'deal_type', 'accommodation_type', 'floor', 'floors_count', 
           'rooms_count', 'total_meters', 'price_per_month', 'commissions', 'price', 'year_of_construction', 
           'object_type', 'house_material_type', 'heating_type', 'finish_type', 'living_meters', 'kitchen_meters', 
           'phone', 'district', 'street', 'house_number', 'underground', 'residential_complex']
selected_columns = exel_export[columns]
selected_columns.to_csv('cianchick.csv', mode='a', header=False, index=False)
