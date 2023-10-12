from time import sleep
from selenium.webdriver.common.by import By    # Елементы
from selenium import webdriver   #  Браузер

driver = webdriver.Chrome()

driver.get("https://ya.ru")

element = driver.find_element(By.CSS_SELECTOR, "#text")    # найти элемент
element.clear()
element.send_keys("test skypro")

driver.find_element(By.CSS_SELECTOR, "body > main > div.body__content > form > div.search3__inner > button").click()

print(element)
#driver.find_elements()    # найти элементы
sleep(5)