import cianparser
import pandas as pd
import time
import logging

# Настраиваем логирование для отслеживания ошибок и прогресса
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_cian(location='Москва', deal_type='sale', rooms=(1, 2), start_page=1, end_page=20, retry_attempts=3, delay=10):
    # Инициализация парсера
    parser = cianparser.CianParser(location=location)
    data = []
    
    for page in range(start_page, end_page + 1):
        attempt = 0
        success = False

        # Повторные попытки при возникновении ошибки клиента
        while attempt < retry_attempts and not success:
            try:
                # Получаем данные с текущей страницы
                flats = parser.get_flats(deal_type=deal_type, rooms=rooms, with_extra_data=True,
                                         additional_settings={'start_page': page, 'end_page': page})
                data.extend(flats)
                logging.info(f"Страница {page} успешно обработана. Найдено объектов: {len(flats)}")
                success = True  # Помечаем успешное завершение
            except Exception as e:
                attempt += 1
                logging.warning(f"Ошибка на странице {page}: {e}. Попытка {attempt} из {retry_attempts}")
                time.sleep(delay)  # Задержка между повторными попытками

        if not success:
            logging.error(f"Не удалось загрузить данные со страницы {page} после {retry_attempts} попыток")

        # Задержка между запросами, чтобы избежать блокировки
        time.sleep(delay)

    return data

def export_to_csv(data, file_name='cian_parsing.csv', mode='a', header=False):
    df = pd.DataFrame(data)
    
    # Список нужных столбцов
    columns = ['author', 'author_type', 'url', 'location', 'deal_type', 'accommodation_type', 'floor', 'floors_count', 
               'rooms_count', 'total_meters', 'price_per_month', 'commissions', 'price', 'year_of_construction', 
               'object_type', 'house_material_type', 'heating_type', 'finish_type', 'living_meters', 'kitchen_meters', 
               'phone', 'district', 'street', 'house_number', 'underground', 'residential_complex']
    
    # Проверка на наличие данных в колонках
    if not df.empty:
        selected_columns = df[columns] if set(columns).issubset(df.columns) else df
        selected_columns.to_csv(file_name, mode=mode, header=header, index=False)
        logging.info(f"Данные успешно экспортированы в {file_name}")
    else:
        logging.warning("Нет данных для экспорта")

if __name__ == "__main__":
    # Параметры для парсинга
    start_page = 1
    end_page = 2
    deal_type = 'sale'  # Тип сделки: продажа
    rooms = (1, 2)      # Количество комнат

    # Парсинг данных
    data = parse_cian(location='Москва', deal_type=deal_type, rooms=rooms, start_page=start_page, end_page=end_page)

    # Экспорт данных в CSV
    export_to_csv(data, file_name='parsed.csv', mode='a', header=True)
