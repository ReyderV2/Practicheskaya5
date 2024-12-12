import requests
from bs4 import BeautifulSoup

# URL страницы
url = "https://www.py4e.com/"

# Получаем содержимое страницы
response = requests.get(url)
response.raise_for_status()  # Проверяем, что запрос успешен

# Парсим HTML с помощью BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Находим все ссылки на странице
links = soup.find_all('a', href=True)

# Собираем уникальные внешние ссылки
external_links = set()
for link in links:
    href = link['href']
    # Проверяем, что ссылка начинается с "http" или "https", но не с "https://www.py4e.com/"
    if href.startswith(('http://', 'https://')) and not href.startswith("https://www.py4e.com/"):
        external_links.add(href)

# Выводим результат
print(f"Количество уникальных внешних ссылок: {len(external_links)}")
print("Список уникальных внешних ссылок:")
for link in external_links:
    print(link)