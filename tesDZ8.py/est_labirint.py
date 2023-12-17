from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys   # кнопки


cookie = {   # убераем окно с куки
        "name": "cookie_policy",
        "value": "1"
    } 

def test_cart_counter():
    driver = webdriver.Chrome()

    #Перейти на сайт лабиринт
    driver.get("https://www.labirint.ru")
    driver.implicitly_wait(4)   # задержка 4 секунды
    driver.maximize_window()   # Браузер на весь экран
    driver.add_cookie(cookie) # убераем окно с куки
    
    #Найти все книги по слову Python
    search_input = driver.find_element(By.CSS_SELECTOR, "#search-field") # Найти эедемент
    search_input.send_keys("Python", Keys.RETURN) # Нажать энтер

    #Переключиться на таблицу
    # Нет перехода в таблицу
    
    #WebDriverWait(driver, 10).until(
    #     EC.presence_of_all_elements_located( (By.CSS_SELECTOR, "#rubric-tab"))
    #) # будет ждать до 10 секунд загрузки сайта(страницы)

    #Добавить все книги в корзину и посчитать, сколько
    buy_buttons = driver.find_elements(By.CSS_SELECTOR, ".product-card__controls-container")
    counter = 0
    for btn in buy_buttons:
         btn.click() # Нажать на все кнопки в цикле
         counter += 1
    print(counter) # 60 раз нажали на кнопку
    #Перейти в корзину
    driver.get("https://www.labirint.ru/cart/")

    #Проверить счетчик товаров. Должен быть равен числу нажатий
    #получить текущее значение
    txt = driver.find_element(By.CSS_SELECTOR, "#ui-id-4").find_element(By.CSS_SELECTOR, "b").text
    
    #сравнить с cuunter
    assert counter == int(txt) # перевели текст в число
    driver.quit()




