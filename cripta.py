import requests

url = "https://api.privatbank.ua/p2p/pubshare/config/tbu"

# Додаємо "паспорт" браузера
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        print("Нарешті успіх!")
        print(response.json())
    else:
        print(f"Статус: {response.status_code}")
        print("Сервер відповів, але не тим, що треба.")
except Exception as e:
    print(f"Сталася помилка з'єднання: {e}")