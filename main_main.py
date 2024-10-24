import json
import requests
import hashlib
import pandas as pd
from datetime import datetime


class DomClickApi:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"X-Service": "true",
                                     "Connection": "Keep-Alive",
                                     "User-Agent": "Android; 12; Google; google_pixel_5; 8.72.0; 8720006; ; NONAUTH"
                                     })

        # Инициализация (получение cookies)
        self.get("https://api.domclick.ru/core/no-auth-zone/api/v1/ensure_session")
        self.get("https://ipoteka.domclick.ru/mobile/v1/feature_toggles")

    def get(self, url, **kwargs):
        self.__update_headers(url, **kwargs)
        result = self.session.get(url, **kwargs)
        print(self.session.cookies.get_dict())
        return result

    def __update_headers(self, url, **kwargs):
        url = self.__get_prepared_url(url, **kwargs)
        sault = "ad65f331b02b90d868cbdd660d82aba0"
        timestamp = str(int(datetime.now().timestamp()))
        encoded = (sault + url + timestamp).encode("UTF-8")
        h = hashlib.md5(encoded).hexdigest()
        self.session.headers.update({"Timestamp": timestamp,
                                     "Hash": "v1:" + h,
                                     })

    def __get_prepared_url(self, url, **kwargs):
        p = requests.models.PreparedRequest()
        p.prepare(method="GET", url=url, **kwargs)
        return p.url


def pprint_json(json_str):
    try:
        json_object = json.loads(json_str)
        json_formatted_str = json.dumps(json_object, indent=2, ensure_ascii=False).encode('utf8')
        print(json_formatted_str.decode())
    except:
        print(json_str)


offers_url = 'https://offers-service.domclick.ru/research/v5/offers/'
count_url = 'https://offers-service.domclick.ru/research/v5/offers/count/'

dca = DomClickApi()
res = dca.get(count_url, params={
    "address": "1d1463ae-c80f-4d19-9331-a1b68a85b553",  # UUID региона
    "deal_type": "sale",  # Тип сделки: Купить
    "category": "living",  # Категория: Жилье
    "offer_type": ["flat", "layout"],  # Тип недвижимости: квартира (вторичка/новостройка)
    "rooms": ["1", "2", "3", "4"],  # Кол-во комнат: 1, 2, 3, 4
    "area__gte": 1,  # Площадь от 1 кв.м
    "floor__gte": 1,  # Этаж от 1
    "sort": "qi",  # Сортировка по рекомендуемым
    "sort_dir": "desc",  # По убыванию
    "offset": 0,
    "limit": 30  # Лимит выборки
})
print("RES:", res)
print(res.text)
pprint_json(res.text)

count_obj = json.loads(res.text)
total = count_obj["pagination"]["total"]

# Инициализация списка для сохранения данных предложений
offers_list = []
offset = 0
max_offset = 2000  # Установлен лимит для offset

while offset < total:
    try:
        if offset > max_offset:
            print(f"Offset {offset} превышает допустимый предел. Пропуск...")
            offset += 20
            continue

        res = dca.get(offers_url, params={
            "address": "1d1463ae-c80f-4d19-9331-a1b68a85b553",
            "deal_type": "sale",
            "category": "living",
            "offer_type": ["flat", "layout"],
            "rooms": ["1", "2", "3", "4"],
            "area__gte": 1,
            "floor__gte": 1,
            "sort": "qi",
            "sort_dir": "desc",
            "offset": offset,
            "limit": 20,  # Лимит уменьшен
        })
        print("RES:", res)
        pprint_json(res.text)

        offers_obj = json.loads(res.text)

        # Пропускаем объявления, если ключи 'result' или 'items' отсутствуют
        if 'result' not in offers_obj or 'items' not in offers_obj['result']:
            print(f"Ключ 'items' или 'result' отсутствует в ответе: {offers_obj}")
            offset += 20
            continue

        offers_list.extend(offers_obj['result']['items'])
        total = offers_obj["pagination"]["total"]
        print(f"{offset}/{total}")
        offset += 20  # Увеличиваем offset для следующей страницы

    except Exception as e:
        print(f"Ошибка при обработке запроса: {e}")
        offset += 20  # Пропускаем текущий запрос и продолжаем

# Преобразование списка предложений в DataFrame
if offers_list:
    exel_export = pd.DataFrame(offers_list)

    # Определяем нужные колонки (проверьте, что все ключи существуют в данных предложений)
    columns = ['renovation', 'placement_type', 'has_big_check', 'offer_type',
               'discount_status', 'developer', 'complex', 'trade_in', 'published_dt',
               'layout_id', 'min_rate', 'status', 'photos', 'chat_available',
               'payment_order_id', 'id', 'object_info', 'backwash', 'source',
               'address', 'offers_count', 'slug', 'is_auction', 'house', 'description',
               'price_info', 'deal_type', 'last_price_history_state', 'ipoteka_rate',
               'monthly_payment', 'legal_options', 'seo_info', 'has_advance_payment',
               'updated_dt', 'seo', 'pessimization', 'duplicates_offer_count',
               'is_placement_paid', 'seller', 'assignment_sale', 'tariff_options',
               'category', 'online_show', 'is_exclusive', 'flat_complex',
               'rooms_offered', 'profit_badge', 'land', 'video']

    available_columns = [col for col in columns if col in exel_export.columns]

    if not available_columns:
        print("Нет совпадающих колонок для экспорта в DataFrame.")
    else:
        selected_columns = exel_export[available_columns]
        selected_columns.to_csv('parsing.csv', mode='a', header=False, index=False)
else:
    print("Нет данных для экспорта.")
