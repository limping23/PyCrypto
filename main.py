import requests
from bs4 import BeautifulSoup
import time

def get_crypto_info(crypto_name):
    url = f"https://www.binance.com/ru/price/{crypto_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Получение текущей стоимости
    price_element = soup.find("div", class_="css-12ujz79")
    if price_element:
        price = price_element.text.strip()
        print(f"Текущая стоимость {crypto_name}: {price}")
    else:
        print(f"Не удалось найти информацию о стоимости {crypto_name}.")

    # Получение рыночной капитализации
    market_cap_element = soup.find("div", class_="css-1o346il")
    if market_cap_element:
        market_cap = market_cap_element.text.strip()
        print(f"Рыночная капитализация {crypto_name}: {market_cap}")
    else:
        print(f"Не удалось найти информацию о рыночной капитализации {crypto_name}.")

# Пример использования
get_crypto_info("ethereum")