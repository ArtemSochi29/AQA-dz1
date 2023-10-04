from time import sleep    # Время работы браузера
from selenium.webdriver.common.by import By    # Елементы
from selenium import webdriver   #  Браузер
driver = webdriver.Chrome()

# Задание 5

# Откройте страницу http://uitestingplayground.com/classattr.
driver.get("http://uitestingplayground.com/classattr")

# Кликните на синюю кнопку.
driver.find_element(By.CSS_SELECTOR, "body > section > div > button.btn-primary").click()

# Запустите скрипт 3 раза подряд. Убедитесь, что он отработает одинаково.
# Запустил 3 раза
sleep(5)