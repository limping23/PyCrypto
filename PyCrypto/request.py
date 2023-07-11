import requests
from bs4 import BeautifulSoup


def request(div, crypto_name):
    url = f"https://www.binance.com/en/price/{crypto_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    element = soup.find("div", class_=div)
    if element:
        element = element.get_text()
        return element
    else:
        return None





