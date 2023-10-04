from time import sleep    # Время работы браузера
from selenium.webdriver.common.by import By    # Елементы
from selenium import webdriver   #  Браузер
driver = webdriver.Chrome()

# Задание 6

# Откройте страницу http://the-internet.herokuapp.com/entry_ad.
driver.get("http://the-internet.herokuapp.com/entry_ad")

# В модальном окне нажмите на кнопку Сlose.
driver.find_element(By.CSS_SELECTOR, "#restart-ad")

sleep(2)

driver.find_element(By.CSS_SELECTOR, "#modal > div.modal > div.modal-footer > p").click()

sleep(2)