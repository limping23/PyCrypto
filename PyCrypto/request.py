import requests
from bs4 import BeautifulSoup
from enums import url


def request(div):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    element = soup.find("div", class_=div).find("span")
    return element



