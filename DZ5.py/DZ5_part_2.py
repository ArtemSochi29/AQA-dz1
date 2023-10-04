from time import sleep    # Время работы браузера
from selenium.webdriver.common.by import By    # Елементы
from selenium import webdriver   #  Браузер
from selenium.webdriver.common.keys import Keys   # кнопки
driver = webdriver.Chrome()
# Фаерфокс браузер
#driver = webdriver.Firefox()
#from selenium.webdriver.firefox.options import Options
#firefox_options = Options()
#driver = webdriver.Firefox(options=firefox_options)

# Задание 6

# Откройте страницу http://the-internet.herokuapp.com/entry_ad.
driver.get("http://the-internet.herokuapp.com/entry_ad")

# В модальном окне нажмите на кнопку Сlose.
driver.find_element(By.CSS_SELECTOR, "#restart-ad")
sleep(2)
driver.find_element(By.CSS_SELECTOR, "#modal > div.modal > div.modal-footer > p").click()
sleep(2)
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

# Задание 8
# Откройте страницу http://the-internet.herokuapp.com/login.
driver.get("http://the-internet.herokuapp.com/login")

# В поле username введите значение `tomsmith`.
username = driver.find_element(By.CSS_SELECTOR, "#username")
username.send_keys("tomsmith")

# В поле password введите значение `SuperSecretPassword!`.
password = driver.find_element(By.CSS_SELECTOR, "#password")
password.send_keys("SuperSecretPassword!")

# Нажмите кнопку `Login`.
driver.find_element(By.CSS_SELECTOR, "#login > button").click()
 
sleep(5)