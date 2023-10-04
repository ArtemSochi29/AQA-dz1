from selenium.webdriver.common.by import By    # Елементы
from selenium import webdriver   #  Браузер
from selenium.webdriver.firefox.options import Options
firefox_options = Options()
driver = webdriver.Firefox(options=firefox_options)
driver = webdriver.Firefox()

# Задание 5

# Откройте страницу http://uitestingplayground.com/classattr.
driver.get("http://uitestingplayground.com/classattr")

# Кликните на синюю кнопку.
driver.find_element(By.CSS_SELECTOR, "body > section > div > button.btn-primary").click()

# Запустите скрипт 3 раза подряд. Убедитесь, что он отработает одинаково.
# Запустил 3 раза
