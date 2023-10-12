from time import sleep
from selenium.webdriver.common.by import By    # Елементы
from selenium import webdriver   #  Браузер

driver = webdriver.Chrome()

my_cookie = {
    'name': 'cookie_policy',
    'value': '1'
}

driver.get("https://labirint.ru")

driver.add_cookie(my_cookie)

cookie = driver.get_cookie('adrdel')
print(cookie)
driver.refresh()
driver.delete_all_cookies()
driver.refresh()


sleep(5)

driver.quit()