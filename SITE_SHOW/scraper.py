import requests
from bs4 import BeautifulSoup

def buscar_eventos():
    url = "https://www.eventbrite.com/d/online/all-events/"
    
    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")

    eventos = []

    for item in soup.find_all("h3"):
        eventos.append(item.text.strip())

    return eventos