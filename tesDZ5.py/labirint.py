
from time import sleep    # Время работы браузера
from selenium.webdriver.common.by import By    # Елементы
from selenium import webdriver   #  Браузер
from selenium.webdriver.common.keys import Keys   # кнопки
driver = webdriver.Chrome()

# Зайти на сайт лабиринт
driver.get("https://www.labirint.ru")

#search_locator = "#search-field"
# Найти книги по слову питон
search_input = driver.find_element(By.CSS_SELECTOR, "#search-field")
search_input.send_keys("Python", Keys.RETURN)
#search_input.send_keys(Keys.RETURN)

# Собрать все карточки товаров
book_locator = "div.product-card"

books = driver.find_elements(By.CSS_SELECTOR, "div.product-card")

# Вывести в консоль инфо: название, автор, цена

for book in books:
    title = book.find_element(By.CSS_SELECTOR, 'a.product-card__name').text
    price = book.find_element(By.CSS_SELECTOR, 'div.product-card__price-current').text

    author = ''
    try:
        author = book.find_element(By.CSS_SELECTOR, 'div.product-card__author').text
    except:
        author = "Автор не указан"
    print("Автор-", author + " Название-" + title + " Цена-" + price)

