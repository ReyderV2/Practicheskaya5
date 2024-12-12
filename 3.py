from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Настройки Selenium
chrome_options = Options()
chrome_options.add_argument("--headless")  # Запуск в фоновом режиме
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

# Инициализация драйвера
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# URL страницы
url = "https://stackoverflow.com/jobs/companies"

# Открываем страницу
driver.get(url)

# Ждем загрузки данных с использованием WebDriverWait
wait = WebDriverWait(driver, 15)  # Увеличиваем время ожидания до 15 секунд
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'flex--item.fs-body3')))

# Находим все элементы <div> с классом 'flex--item.fs-body3'
div_elements = driver.find_elements(By.CLASS_NAME, 'flex--item.fs-body3')

# Находим все элементы с городами
cities = set()  # Используем множество для хранения уникальных городов

# Пример поиска городов
for div in div_elements:
    # Проверяем, содержит ли элемент класс 'fc-black-500'
    if 'fc-black-500' in div.get_attribute('class'):
        city = div.text.strip()
        if city:
            cities.add(city)

# Сортируем города в алфавитном порядке
sorted_cities = sorted(cities)

# Выводим результат
print("Города без повторов в алфавитном порядке:")
for city in sorted_cities:
    print(city)

# Закрываем браузер
driver.quit()