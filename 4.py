from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def find_questions(keyword, pages_to_search=5):
    chrome_options = Options()
    chrome_options.add_argument("--ignore-certificate-errors")
    chrome_options.add_argument("--headless")  
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    base_url = "https://stackoverflow.com/questions"

    questions = []

    try:
        for page in range(1, pages_to_search + 1):
            url = f"{base_url}?page={page}&sort=newest"
            driver.get(url)
            wait = WebDriverWait(driver, 10)
            wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 's-post-summary')))

            for question in driver.find_elements(By.CLASS_NAME, 's-post-summary'):
                title_element = question.find_element(By.CLASS_NAME, 's-link')
                title = title_element.text
                link = title_element.get_attribute('href')
                if keyword.lower() in title.lower():
                    questions.append((title, link))

    finally:
        driver.quit()

    return questions

if __name__ == "__main__":
    keyword = input("Введите ключевое слово для поиска вопросов: ")
    pages_to_search = int(input("Введите количество страниц для поиска (5-20): "))

    if pages_to_search < 5 or pages_to_search > 20:
        print("Количество страниц должно быть от 5 до 20.")
    else:
        results = find_questions(keyword, pages_to_search)

        if results:
            print(f"Найдено {len(results)} вопросов с ключевым словом '{keyword}':")
            for title, link in results:
                print(f"Заголовок: {title}")
                print(f"Ссылка: {link}")
                print("-" * 80)
        else:
            print(f"Вопросов с ключевым словом '{keyword}' не найдено.")