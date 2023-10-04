from time import sleep    # Время работы браузера
from selenium.webdriver.common.by import By    # Елементы
from selenium import webdriver   #  Браузер
driver = webdriver.Chrome()

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