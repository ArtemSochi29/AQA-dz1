from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By   
from selenium import webdriver  
from selenium.webdriver.common.keys import Keys   # кнопки
from time import sleep

cookie = {   # убераем окно с куки
        "name": "cookie_policy",
        "value": "1"
    } 

driver = None

def open_labirint():
#Перейти на сайт лабиринт
    driver.get("https://www.labirint.ru")
    driver.implicitly_wait(4)   # задержка 4 секунды
    driver.maximize_window()   # Браузер на весь экран
    driver.add_cookie(cookie) # убераем окно с куки

def search(tern):
#Найти все книги по слову Python
    search_input = driver.find_element(By.CSS_SELECTOR, "#search-field") # Найти эедемент
    search_input.send_keys(tern, Keys.RETURN) # Нажать энтер

#def swich_to_table():
#Переключиться на таблицу
# Нет перехода в таблицу
#    driver.find_element(By.CSS_SELECTOR, "a[title='таблицей']").click()
#    WebDriverWait(driver, 10).until(
#         EC.presence_of_all_elements_located( (By.CSS_SELECTOR, "#rubric-tab"))
#    ) # будет ждать до 10 секунд загрузки сайта(страницы)

def add_books():
#Добавить все книги в корзину и посчитать, сколько
    buy_buttons = driver.find_elements(By.CSS_SELECTOR, ".product-card__controls-container")
    counter = 0
    for btn in buy_buttons:
         btn.click() # Нажать на все кнопки в цикле
         counter += 1
    
    return counter

def go_to_cart():
#Перейти в корзину
    driver.get("https://www.labirint.ru/cart/")

def get_cart_counter():
#Проверить счетчик товаров. Должен быть равен числу нажатий
#получить текущее значение
    txt = driver.find_element(By.CSS_SELECTOR, "#ui-id-4").find_element(By.CSS_SELECTOR, "b").text
    return int(txt)

def close_driver():
#Закрыть браузер
    driver.quit()

def est_cart_counter():
    driver = webdriver.Chrome()
    open_labirint()
    search("Python")
    #switch_to_table()

    added = add_books()
    go_to_cart()
    cart_counter = get_cart_counter()
    close_driver()

    assert added == cart_counter

def est_empty_search():
    open_labirint()
    search("no book search")
    txt = driver.find_elements(By.CSS_SELECTOR, "#right-inner")
    assert txt == 'Все, что мы нашли в Лабиринте по запросу «no book search»'


