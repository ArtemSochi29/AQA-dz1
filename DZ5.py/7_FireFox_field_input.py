from selenium.webdriver.common.by import By    # Елементы
from selenium import webdriver   #  Браузер
from selenium.webdriver.firefox.options import Options
firefox_options = Options()
driver = webdriver.Firefox(options=firefox_options)
driver = webdriver.Firefox()

# Задание 7
# Откройте страницу http://the-internet.herokuapp.com/inputs.
driver.get("http://the-internet.herokuapp.com/inputs")

# Введите в поле текст `1000`.
entry_field = driver.find_element(By.CSS_SELECTOR, "#content > div > div > div > input[type=number]")
entry_field.send_keys("1000")

# Очистите это поле (метод `clear`).
entry_field.clear()

# Введите в это же поле текст `999`.
entry_field.send_keys("999")
