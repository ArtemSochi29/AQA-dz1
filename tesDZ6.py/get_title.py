from selenium.webdriver.common.by import By    # Елементы
from selenium import webdriver   #  Браузер

driver = webdriver.Chrome()

driver.get("https://rzd.ru")

current_title = driver.title

print(current_title)

driver.quit()

