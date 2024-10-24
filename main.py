import cianparser
import csv
import time
import random

def save_to_csv(flats_data, filename="zxc.csv"):
    keys = flats_data[0].keys()
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=keys)
        writer.writerows(flats_data)

def fetch_flats(parser, page):
    try:
        data = parser.get_flats(deal_type="sale", rooms=(1), additional_settings={"start_page": page, "end_page": page})
        
        print(data)
        
        print('--------------------------------------------------------------------------')
        
        for flat in data:
            
            flat['author'] = flat.get('author', 'Не указано')
            flat['author_type'] = flat.get('author_type', 'Не указано')
            flat['location'] = flat.get('location', 'Не указано')
            flat['deal_type'] = flat.get('deal_type', 'Не указано')
            flat['accommodation_type'] = flat.get('accommodation_type', 'Не указано')
            flat['rooms_count'] = flat.get('rooms_count', 'Не указано')
            flat['total_meters'] = flat.get('total_meters', 'Не указано')
            flat['price'] = flat.get('price', 'Не указано')
            flat['year_of_construction'] = flat.get('year_of_construction', 'Не указано')
            flat['object_type'] = flat.get('object_type', 'Не указано')
            flat['house_material_type'] = flat.get('house_material_type', 'Не указано')
            flat['heating_type'] = flat.get('heating_type', 'Не указано')
            flat['finish_type'] = flat.get('finish_type', 'Не указано')
            flat['living_meters'] = flat.get('living_meters', 'Не указано')
            flat['kitchen_meters'] = flat.get('kitchen_meters', 'Не указано')
            flat['street'] = flat.get('street', 'Не указано')
            flat['house_number'] = flat.get('house_number', 'Не указано')
            flat['underground'] = flat.get('underground', 'Не указано')
            flat['residential_complex'] = flat.get('residential_complex', 'Не указано')
            flat['floor'] = flat.get('floor', 'Не указано')
            flat['floors_count'] = flat.get('floors_count', 'Не указано')
            flat['url'] = flat.get('url', 'Не указано')

        return data
    except Exception as e:
        print(f"Ошибка на странице {page}: {e}")
        return []

parser = cianparser.CianParser(location="Долгопрудный")

for page in range(1, 1000):
    flats = fetch_flats(parser, page)
    if not flats:
        break
    save_to_csv(flats)
    time.sleep(random.uniform(3, 6))

print("Парсинг завершён.")
