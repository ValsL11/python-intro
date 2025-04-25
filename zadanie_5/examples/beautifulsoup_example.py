from bs4 import BeautifulSoup
import requests

# Pobranie strony internetowej
url = "https://example.com"
response = requests.get(url)

# Parsowanie HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Wyszukiwanie tytułu strony
title = soup.title.string
print("Tytuł strony:", title)

# Wyszukiwanie wszystkich linków
links = soup.find_all('a')
for link in links:
    print(link.get('href'))