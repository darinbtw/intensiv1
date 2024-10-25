import pandas as pd
import requests

# Токен API (замените на ваш, если он активен)
token = 'O4sgQSKhTCqC0PAuHKDFaQWMRh2V_B0IPbAjYjDa'

# Тестовый URL — уточните его в документации Avito API
test_url = "https://api.avito.ru/v2/accounts/self"  # Например, для получения информации о текущем аккаунте

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(test_url, headers=headers)

if response.status_code == 200:
    print("Подключение успешно! Ответ:", response.json())
else:
    print(f"Ошибка подключения: {response.status_code}, {response.text}")

