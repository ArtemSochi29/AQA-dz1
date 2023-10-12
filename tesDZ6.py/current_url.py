from selenium.webdriver.common.by import By    # Елементы
from selenium import webdriver   #  Браузер

driver = webdriver.Chrome()

driver.get("http://ya.ru")

url = driver.current_url

print(url)

driver.quit()