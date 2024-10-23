import pandas as pd
import os
import cianparser

# Функция для парсинга данных с ЦИАН
def parse_cian():
    cian = Cian()
    
    # Параметры поиска объявлений (например, квартиры на продажу)
    results = cian.search(
        deal_type='sale',           # Тип сделки: 'sale' - продажа
        accommodation_type='flat',  # Тип жилья: квартира
        region='Москва'             # Регион (например, Москва)
    )

    data = []

    # Обработка результатов
    for result in results:
        data.append({
            'author': result.get('author'),  # Продавец
            'author_type': result.get('author_type'),  # Тип продавца (агент, частное лицо)
            'location': result.get('location'),  # Полное местоположение
            'deal_type': result.get('deal_type'),  # Тип сделки
            'accommodation_type': result.get('accommodation_type'),  # Тип недвижимости (квартира, дом и т.д.)
            'floors_count': result.get('floors_count'),  # Количество этажей
            'rooms_count': result.get('rooms_count'),  # Количество комнат
            'total_meters': result.get('total_meters'),  # Общая площадь в метрах
            'price': result.get('price'),  # Цена
            'district': result.get('district'),  # Район
            'street': result.get('street'),  # Улица
            'house_number': result.get('house_number'),  # Номер дома
            'underground': result.get('underground'),  # Станция метро
            'residential_complex': result.get('residential_complex')  # Жилой комплекс
        })

    return data

# Функция для сохранения данных в CSV
def save_to_csv(data, filename='output.csv'):
    if os.path.exists(filename):
        # Читаем существующий файл и добавляем новые данные
        existing_data = pd.read_csv(filename)
        new_data = pd.DataFrame(data)
        combined_data = pd.concat([existing_data, new_data]).drop_duplicates()
    else:
        # Если файл не существует, создаём новый
        combined_data = pd.DataFrame(data)

    # Сохраняем данные в CSV без индексов
    combined_data.to_csv(filename, index=False)

# Основной код
parsed_data = parse_cian()
save_to_csv(parsed_data)
