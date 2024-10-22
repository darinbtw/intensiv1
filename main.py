import cianparser
import pandas

moscow = cianparser.CianParser(location='Москва')
data = moscow.get_flats(deal_type='sale', rooms=(3), additional_settings={'start_page': 1, 'end_page':1} )
sorted_price = sorted(data, key=lambda x: x['price'])
# print(sorted_price)

export_e

for apartment in sorted_price:
    print(f'Автор: {apartment["author"]}  {apartment["author_type"]} Ссылка: {apartment["url"]} Локация: {apartment["location"]} '
          f'Тип сортировки: {apartment["deal_type"]} {apartment["accommodation_type"]} Этаж: {apartment["floor"]} {apartment["floors_count"]} Квартира: {apartment["rooms_count"]} '
          f'Всего метров: {apartment["total_meters"]} Цена: {apartment["price"]} Район: {apartment["district"]} Улица: {apartment["street"]} {apartment["house_number"]} '
          f'{apartment["underground"]} {apartment["residential_complex"]}')

