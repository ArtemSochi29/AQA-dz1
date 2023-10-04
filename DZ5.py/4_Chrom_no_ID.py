from time import sleep    # Время работы браузера
from selenium.webdriver.common.by import By    # Елементы
from selenium import webdriver   #  Браузер
driver = webdriver.Chrome()

# Задание 4

# Откройте страницу http://uitestingplayground.com/dynamicid.
driver.get("http://uitestingplayground.com/dynamicid")

# Кликните на синюю кнопку.
driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

# Запустите скрипт 3 раза подряд. Убедитесь, что он отработает одинаково.
# Запустил 3 раза подряд