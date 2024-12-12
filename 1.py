import requests
from bs4 import BeautifulSoup

url = "https://www.py4e.com/"

response = requests.get(url)
response.raise_for_status()  

soup = BeautifulSoup(response.text, 'html.parser')

links = soup.find_all('a', href=True)

external_links = set()
for link in links:
    href = link['href']
    if href.startswith(('http://', 'https://')) and not href.startswith("https://www.py4e.com/"):
        external_links.add(href)

print(f"Количество уникальных внешних ссылок: {len(external_links)}")
print("Список уникальных внешних ссылок:")
for link in external_links:
    print(link)