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

# Задание 3

# 1 Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/.
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

#a = driver.find_element (By.XPATH, "//*[@id='content']/div/button").click()

# 2 Пять раз кликните на кнопку Add Element.
button_loc = "//*[@id='content']/div/button"
click_button = driver.find_element(By.XPATH, button_loc).click()
click_button = driver.find_element(By.XPATH, button_loc).click()
click_button = driver.find_element(By.XPATH, button_loc).click()
click_button = driver.find_element(By.XPATH, button_loc).click()
click_button = driver.find_element(By.XPATH, button_loc).click()

# 3 Соберите со страницы список кнопок Delete.
element_loc = ("button[onclick='deleteElement()']")
elements = driver.find_elements(By.CSS_SELECTOR, element_loc)

# 4 Выведите на экран размер списка.
amount_elements = driver.find_elements(By.CSS_SELECTOR, element_loc)

print(len(amount_elements))

# Задание 4

# Откройте страницу http://uitestingplayground.com/dynamicid.
driver.get("http://uitestingplayground.com/dynamicid")

# Кликните на синюю кнопку.
driver.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()

# Запустите скрипт 3 раза подряд. Убедитесь, что он отработает одинаково.
# Запустил 3 раза подряд

# Задание 5

# Откройте страницу http://uitestingplayground.com/classattr.
driver.get("http://uitestingplayground.com/classattr")

# Кликните на синюю кнопку.
driver.find_element(By.CSS_SELECTOR, "body > section > div > button.btn-primary").click()

# Запустите скрипт 3 раза подряд. Убедитесь, что он отработает одинаково.
# Запустил 3 раза

sleep(2)