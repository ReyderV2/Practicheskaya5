from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

url = "https://stackoverflow.com/jobs/companies"


driver.get(url)

wait = WebDriverWait(driver, 15) 
wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'flex--item.fs-body3')))


div_elements = driver.find_elements(By.CLASS_NAME, 'flex--item.fs-body3')

cities = set()  

for div in div_elements:
    if 'fc-black-500' in div.get_attribute('class'):
        city = div.text.strip()
        if city:
            cities.add(city)

sorted_cities = sorted(cities)

print("Города без повторов в алфавитном порядке:")
for city in sorted_cities:
    print(city)

driver.quit()