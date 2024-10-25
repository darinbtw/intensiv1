import requests

client_id = 'QTGwo18203s5w5ndbmTo'  # Замените на ваш Client ID
client_secret = 'bgzubdFRutBm7hTuA43YUlcadKgAkFHglJ3nr9VV'  # Замените на ваш Client Secret

# URL для получения токена
token_url = "https://api.avito.ru/token/"

# Данные для запроса токена
data = {
    'client_id': client_id,
    'client_secret': client_secret,
    'grant_type': 'client_credentials'
}

# Запрос токена
response = requests.post(token_url, data=data)
token = response.json().get("access_token")

print("Получен токен:", token)
