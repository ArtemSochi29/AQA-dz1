from time import sleep    # Время работы браузера
from selenium.webdriver.common.by import By    # Елементы
from selenium import webdriver   #  Браузер
driver = webdriver.Chrome()


# Задание 3

# 1 Откройте страницу http://the-internet.herokuapp.com/add_remove_elements/.
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")

#a = driver.find_element (By.XPATH, "//*[@id='content']/div/button").click()

# 2 Пять раз кликните на кнопку Add Element.
button_loc = "//*[@id='content']/div/button"

for iterator in range(5):
    driver.find_element(By.XPATH, button_loc).click()

# 3 Соберите со страницы список кнопок Delete.
element_loc = ("button[onclick='deleteElement()']")
elements = driver.find_elements(By.CSS_SELECTOR, element_loc)

# 4 Выведите на экран размер списка.
amount_elements = driver.find_elements(By.CSS_SELECTOR, element_loc)

print(len(amount_elements))

sleep(3)